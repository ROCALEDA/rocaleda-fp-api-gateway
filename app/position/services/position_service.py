from fastapi import Request, HTTPException

from app.commons.auth import extract_token, validate_token
from app.position.repositories.position_repository import PositionRepository


class PositionService:
    def __init__(self, position_repository: PositionRepository):
        self.position_repository = position_repository

    async def get_closed_positions_with_candidates(
        self, request: Request, project_id: int
    ):
        try:
            return await self.position_repository.get_closed_positions_with_candidates(
                request, project_id
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def create_evaluation(self, request: Request):
        try:
            return await self.position_repository.create_evaluation(request)
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error") from e

    async def get_positions(self, request: Request):
        try:
            return await self.position_repository.get_positions(request)
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def get_position_candidates_info(self, request: Request, position_id: int):
        try:
            received_token = extract_token(request)
            await validate_token(request, received_token)
            return await self.position_repository.get_position_candidates_info(
                request, position_id
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def update_position_chosen_candidate(
        self, request: Request, position_id: int
    ):
        try:
            received_token = extract_token(request)
            await validate_token(request, received_token)
            return await self.position_repository.update_position_chosen_candidate(
                request, position_id
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def save_technical_test_result(self, request: Request, position_id: int):
        try:
            received_token = extract_token(request)
            await validate_token(request, received_token)
            return await self.position_repository.save_technical_test_result(
                request, position_id
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def create_candidate_in_position(self, position_id: int, candidate_id: int):
        try:
            return await self.position_repository.create_candidate_in_position(
                position_id, candidate_id
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error") from e
