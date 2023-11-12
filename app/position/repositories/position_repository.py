import httpx
from fastapi import HTTPException, Request

from app.commons.helpers import build_request_uri
from app.commons.settings import settings


class PositionRepository:
    async def get_positions(self, request: Request):
        async with httpx.AsyncClient() as client:
            uri = build_request_uri(settings.customers_ms, "positions")
            print(f"Sending {request.query_params} to GET {uri}")
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
            print(f"Sending {request.query_params} to GET {uri}")
            response = await client.get(uri, timeout=60)
            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )

            return response.json()

    async def update_position_chosen_candidate(
        self, request: Request, position_id: int
    ):
        async with httpx.AsyncClient() as client:
            body = await request.json()
            uri = build_request_uri(settings.customers_ms, f"positions/{position_id}")
            print(f"Sending {body} to PATCH {uri}")
            response = await client.patch(uri, json=body, timeout=60)
            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()

    async def get_closed_positions_with_candidates(
        self, request: Request, project_id: int
    ):
        async with httpx.AsyncClient() as client:
            uri = build_request_uri(settings.orchestrator_ms, f"positions/{project_id}")
            print(
                f"Sending get closed positions with project id {project_id} to GET {uri}"
            )
            response = await client.get(uri, timeout=60)
            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()

    async def create_evaluation(self, request: Request):
        async with httpx.AsyncClient() as client:
            body = await request.json()
            uri = build_request_uri(settings.customers_ms, "positions/evaluations")
            print(f"Sending {body} to POST {uri}")
            response = await client.post(uri, json=body, timeout=60)
            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()
