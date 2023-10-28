from fastapi import APIRouter, Request

from app.customer.services.customer_service import CustomerService

router = APIRouter(
    prefix="/customer",
    tags=["customer"],
    responses={404: {"description": "Not found"}},
)


def initialize(customer_service: CustomerService):
    @router.post("")
    async def create_customer(request: Request):
        return await customer_service.create_customer(request)

    @router.post("/project")
    async def create_project(request: Request):
        return await customer_service.create_project(request)

    @router.get("/projects")
    async def get_customer_projects(request: Request):
        return await customer_service.get_customer_projects(request)
