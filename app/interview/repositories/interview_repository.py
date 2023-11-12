import httpx
from fastapi import HTTPException, Request

from app.commons.helpers import build_request_uri
from app.commons.settings import settings


class InterviewRepository:
    async def get_interviews_paginated(self, role: str, user_id: str, request: Request):
        async with httpx.AsyncClient() as client:
            uri = build_request_uri(settings.candidates_ms, "interviews")
            reroute_headers = {"role": role}
            reroute_params = {
                "user_id": user_id,
            }
            if len(request.query_params.get("page")) > 0:
                reroute_params["page"] = request.query_params.get("page")
            if len(request.query_params.get("limit")) > 0:
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
