from fastapi import Request

from app.candidate.repositories.candidate_repository import CandidateRepository


class CandidateService:
    def __init__(self, candidate_repository: CandidateRepository):
        self.candidate_repository = candidate_repository

    async def create_candidate(self, request: Request):
        return await self.candidate_repository.create_candidate(request)
