from fastapi import APIRouter, Depends, Request
from app.commons.auth import validate_token

from app.position.services.position_service import PositionService

router = APIRouter(
    prefix="/positions",
    tags=["positions"],
    responses={404: {"description": "Not found"}},
)


def initialize(position_service: PositionService):
    @router.get("")
    async def get_positions(request: Request, _=Depends(validate_token)):
        return await position_service.get_positions(request)
