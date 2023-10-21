from fastapi import Request

from app.customer.repositories.customer_repository import CustomerRepository
from app.commons.auth import extract_token, validate_token


class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    async def create_customer(self, request: Request):
        return await self.customer_repository.create_customer(request)

    async def create_project(self, request: Request):
        received_token = extract_token(request)
        await validate_token(request, received_token)
        print(request.state)
        return await self.customer_repository.create_project(request)
