import httpx
from fastapi import Request
from fastapi import HTTPException
from app.commons.helpers import build_request_uri

from app.commons.settings import settings


class CandidateRepository:
    async def create_candidate(self, request: Request):
        async with httpx.AsyncClient() as client:
            body = await request.json()
            uri = build_request_uri(settings.users_ms, "user/candidate")
            print(f"Sending {body} to {uri}")
            response = await client.post(uri, json=body, timeout=60)

            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()
