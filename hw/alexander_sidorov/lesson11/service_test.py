from typing import Any

import httpx
import pytest
from fastapi import status

from hw.alexander_sidorov.common import ApiResult
from hw.alexander_sidorov.lesson11.util import get_localhost


@pytest.mark.asyncio
async def test_service_index(asgi_client: httpx.AsyncClient) -> None:
    resp: httpx.Response = await asgi_client.get("/")
    assert resp.status_code == status.HTTP_200_OK

    body = resp.text
    assert body.startswith("<!DOCTYPE html>")


@pytest.mark.asyncio
async def test_service_api_10_04(asgi_client: httpx.AsyncClient) -> None:
    resp: httpx.Response

    resp = await asgi_client.get("/api/10/04")
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    result = ApiResult.parse_obj(resp.json())
    assert result.errors == [""]

    resp = await asgi_client.post("/api/10/04", json={"v_int": 10})
    assert resp.status_code == status.HTTP_200_OK

    resp = await asgi_client.post("/api/10/04", json={"v_str": "x"})
    assert resp.status_code == status.HTTP_200_OK

    resp = await asgi_client.get("/api/10/04")
    assert resp.status_code == status.HTTP_200_OK

    result = ApiResult.parse_obj(resp.json())
    assert result.data == "xxxxxxxxxx"

    resp = await asgi_client.post("/api/10/04", json={"v_int": 0})
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    result = ApiResult.parse_obj(resp.json())
    assert result.errors == ["no value given"]


def test_requests_mock(mocker: Any) -> None:
    mock_resp = mocker.Mock()
    mock_resp.text = "xxx"
    mock_httpx_get = mocker.patch(
        "hw.alexander_sidorov.lesson11.util.httpx.get"
    )
    mock_httpx_get.return_value = mock_resp

    assert get_localhost() == "xxx"
    mock_httpx_get.assert_called_once()
