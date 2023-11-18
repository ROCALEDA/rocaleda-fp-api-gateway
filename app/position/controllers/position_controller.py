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

    @router.get("/closed/{project_id}")
    async def get_closed_positions_with_candidates(
        request: Request, project_id: int, _=Depends(validate_token)
    ):
        return await position_service.get_closed_positions_with_candidates(
            request, project_id
        )

    @router.post("/evaluations")
    async def create_evaluation(request: Request, _=Depends(validate_token)):
        return await position_service.create_evaluation(request)

    @router.get("/{position_id}/candidates")
    async def get_position_candidates_info(request: Request, position_id: int):
        return await position_service.get_position_candidates_info(request, position_id)

    @router.patch("/{position_id}")
    async def update_position_chosen_candidate(request: Request, position_id: int):
        return await position_service.update_position_chosen_candidate(
            request, position_id
        )

    @router.post("/{position_id}/candidates/{candidate_id}")
    async def create_candidate_in_position(
        request: Request, position_id: int, candidate_id: int, _=Depends(validate_token)
    ):
        return await position_service.create_candidate_in_position(
            position_id, candidate_id
        )

    @router.post("/{position_id}/tests")
    async def save_technical_test_result(request: Request, position_id: int):
        return await position_service.save_technical_test_result(request, position_id)
