from fastapi import Request, HTTPException

from app.candidate.repositories.candidate_repository import CandidateRepository


class CandidateService:
    def __init__(self, candidate_repository: CandidateRepository):
        self.candidate_repository = candidate_repository

    async def create_candidate(self, request: Request):
        try:
            return await self.candidate_repository.create_candidate(request)
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def get_candidates_paginated(self, request: Request):
        try:
            return await self.candidate_repository.get_candidates_paginated(request)
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")
