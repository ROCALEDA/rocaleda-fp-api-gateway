from fastapi import Request, HTTPException

from app.commons.auth import extract_token, validate_token
from app.customer.repositories.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    async def create_customer(self, request: Request):
        try:
            return await self.customer_repository.create_customer(request)
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def create_project(self, request: Request):
        try:
            received_token = extract_token(request)
            await validate_token(request, received_token)
            return await self.customer_repository.create_project(
                request.state.user_data["user_id"], request
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def get_customer_projects(self, request: Request):
        try:
            received_token = extract_token(request)
            await validate_token(request, received_token)
            return await self.customer_repository.get_customer_projects(
                request.state.user_data["user_id"], request
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def get_customer_performance_evaluations(self, request: Request):
        try:
            received_token = extract_token(request)
            await validate_token(request, received_token)
            return await self.customer_repository.get_customer_performance_evaluations(
                request.state.user_data["user_id"], request
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error") from e

    async def get_candidate_performance_evaluations(self, request: Request):
        try:
            received_token = extract_token(request)
            await validate_token(request, received_token)
            return await self.customer_repository.get_candidate_performance_evaluations(
                request.state.user_data["user_id"], request
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error") from e
