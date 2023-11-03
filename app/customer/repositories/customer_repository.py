import httpx
from fastapi import HTTPException, Request

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
            body = await request.json()
            uri = build_request_uri(
                settings.customers_ms, f"customers/{customer_id}/projects"
            )
            print(f"Sending {body} to {uri}")
            response = await client.post(uri, json=body, timeout=60)

            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()

    async def get_customer_projects(self, customer_id: int, request: Request):
        async with httpx.AsyncClient() as client:
            uri = build_request_uri(
                settings.customers_ms, f"customers/{customer_id}/projects"
            )
            print(f"Sending {request.query_params} to {uri}")
            response = await client.get(uri, params=request.query_params, timeout=60)

            if 400 <= response.status_code < 600:
                error_detail = response.json().get("detail", response.text)
                raise HTTPException(
                    status_code=response.status_code, detail=error_detail
                )
            return response.json()
