from fastapi import Request, HTTPException

from app.commons.auth import extract_token, validate_token
from app.position.repositories.position_repository import PositionRepository


class PositionService:
    def __init__(self, position_repository: PositionRepository):
        self.position_repository = position_repository

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
