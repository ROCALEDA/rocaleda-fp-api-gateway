from fastapi import Request

from app.customer.repositories.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    async def create_customer(self, request: Request):
        return await self.customer_repository.create_customer(request)
