from typing import AsyncGenerator

import httpx
import pytest

from hw.alexander_sidorov.lesson11.service import app

TIMEOUT = 4


@pytest.fixture(scope="function")
async def asgi_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    ctx = httpx.AsyncClient(
        app=app,
        base_url="http://asgi",
        timeout=TIMEOUT,
    )

    async with ctx as client:
        yield client
