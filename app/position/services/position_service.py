from fastapi import Request, HTTPException

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
