from pathlib import Path
from typing import Any
from typing import Optional
from typing import Union

from fastapi import FastAPI
from fastapi import status
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pydantic import Field

from hw.alexander_sidorov.common import ApiResult
from hw.alexander_sidorov.lesson10.homework import Multiplier04

here = Path(__file__).parent.resolve()
dir_static = here / "static"
assert dir_static.is_dir()

app = FastAPI()
app.mount("/s", StaticFiles(directory=dir_static), name="static")


@app.get("/")
def handle_index() -> FileResponse:
    return FileResponse(dir_static / "index.html")


mult = Multiplier04()


@app.get("/api/10/04")
def handle_multiply_get_result() -> Union[ApiResult, JSONResponse]:
    try:
        value = mult.get_result()
        return ApiResult(data=value)
    except Exception as err:  # pylint: disable=broad-except
        return JSONResponse(
            content=ApiResult(errors=[str(err)]).dict(),
            status_code=status.HTTP_400_BAD_REQUEST,
        )


class MultArg(BaseModel):
    v_int: Optional[int] = Field(None)
    v_float: Optional[float] = Field(None)
    v_str: Optional[str] = Field(None)

    def dict(self, **kw: Any) -> dict:  # noqa: A003
        kw["exclude_unset"] = True
        return super().dict(**kw)


@app.post("/api/10/04")
def handle_multiply_add(data: MultArg) -> Union[ApiResult, JSONResponse]:
    try:
        value = [v for _k, v in data.dict().items() if v]
        assert value, "no value given"

        value = value[0]
        assert isinstance(value, (str, int)), "unsupported value type"

        mult.add(value)
        return ApiResult(data={"ok": True})

    except Exception as err:  # pylint: disable=broad-except
        return JSONResponse(
            content=ApiResult(errors=[str(err)]).dict(),
            status_code=status.HTTP_400_BAD_REQUEST,
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "hw.alexander_sidorov.lesson11.service:app",
        host="0.0.0.0",  # noqa: S104
        reload=True,
    )
