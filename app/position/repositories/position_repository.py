import httpx
from fastapi import Request
from fastapi import HTTPException

from app.commons.helpers import build_request_uri
from app.commons.settings import settings


class PositionRepository:
    async def get_positions(self, request: Request):
        async with httpx.AsyncClient() as client:
            uri = build_request_uri(settings.customers_ms, "positions")
            response = await client.get(uri, timeout=60)

            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )

            return response.json()

    async def get_position_candidates_info(self, request: Request, position_id: int):
        async with httpx.AsyncClient() as client:
            uri = build_request_uri(
                settings.orchestrator_ms, f"positions/{position_id}/candidates"
            )
            response = await client.get(uri, timeout=60)

            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )

            return response.json()
