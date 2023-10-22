import httpx
from fastapi import Request
from fastapi import HTTPException

from app.commons.helpers import build_request_uri
from app.commons.settings import settings


class CustomerRepository:
    async def create_customer(self, request: Request):
        async with httpx.AsyncClient() as client:
            body = await request.json()
            uri = build_request_uri(settings.users_ms, "user/customer")
            print(f"Sending {body} to {uri}")
            response = await client.post(uri, json=body, timeout=60)

            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()

    async def create_project(self, customer_id: int, request: Request):
        async with httpx.AsyncClient() as client:
            try:
                body = await request.json()
                uri = build_request_uri(
                    settings.customers_ms, f"customer/{customer_id}/project"
                )
                print(f"Sending {body} to {uri}")
                response = await client.post(uri, json=body, timeout=60)

                if 400 <= response.status_code < 600:
                    raise HTTPException(
                        status_code=response.status_code, detail=response.text
                    )
                return response.json()
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail="Internal Server Error",
                )
