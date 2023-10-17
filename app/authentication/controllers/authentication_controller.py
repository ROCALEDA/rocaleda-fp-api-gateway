from typing import TYPE_CHECKING
from fastapi import APIRouter, Request


if TYPE_CHECKING:
    from app.authentication.services.authentication_service import AuthenticationService


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


def initialize(authentication_service: "AuthenticationService"):
    @router.post("")
    async def get_jwt_token(request: Request):
        return await authentication_service.get_jwt_token(request)

    return {"get_jwt_token": get_jwt_token}
