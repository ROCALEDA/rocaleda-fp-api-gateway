import httpx
from fastapi import HTTPException, Request

from app.commons.helpers import build_request_uri
from app.commons.settings import settings


class InterviewRepository:
    async def get_interviews_paginated(self, role: int, user_id: int, request: Request):
        async with httpx.AsyncClient() as client:
            uri = build_request_uri(settings.candidates_ms, "interviews")
            request.headers["role"] = role
            request.query_params["user_id"] = user_id
            print(f"Sending {request.query_params} and {request.headers} to GET {uri}")
            response = await client.get(
                uri, params=request.query_params, headers=request.headers, timeout=60
            )
            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()
