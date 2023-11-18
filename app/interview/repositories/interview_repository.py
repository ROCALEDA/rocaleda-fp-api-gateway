import httpx
from fastapi import HTTPException, Request

from app.commons.helpers import build_request_uri
from app.commons.settings import settings


class InterviewRepository:
    async def get_interviews_paginated(self, role: str, user_id: str, request: Request):
        async with httpx.AsyncClient() as client:
            uri = build_request_uri(settings.orchestrator_ms, "interviews")
            reroute_headers = {"role": role}
            reroute_params = {
                "user_id": user_id,
            }
            if request.query_params.get("page") is not None:
                reroute_params["page"] = request.query_params.get("page")
            if request.query_params.get("limit") is not None:
                reroute_params["limit"] = request.query_params.get("limit")
            print(
                f"Sending params {reroute_params} and headers {reroute_headers} to GET {uri}"
            )
            response = await client.get(
                uri, params=reroute_params, headers=reroute_headers, timeout=60
            )
            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()

    async def create_interview(self, request: Request):
        async with httpx.AsyncClient() as client:
            body = await request.json()
            uri = build_request_uri(settings.candidates_ms, "interviews")
            print(f"Sending {body} to {uri}")
            response = await client.post(uri, json=body, timeout=60)

            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()
