from fastapi import APIRouter, Depends, Request

from app.candidate.services.candidate_service import CandidateService
from app.commons.auth import validate_token

router = APIRouter(
    prefix="/candidate",
    tags=["candidate"],
    responses={404: {"description": "Not found"}},
)


def initialize(candidate_service: CandidateService):
    @router.post("")
    async def create_candidate(request: Request):
        return await candidate_service.create_candidate(request)

    @router.get("")
    async def get_candidates_paginated(request: Request, _=Depends(validate_token)):
        return await candidate_service.get_candidates_paginated(request)
