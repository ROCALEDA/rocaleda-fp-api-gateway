from fastapi import APIRouter, Request

from app.candidate.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidate",
    tags=["candidate"],
    responses={404: {"description": "Not found"}},
)


def initialize(candidate_service: CandidateService):
    @router.post("")
    async def create_candidate(request: Request):
        return await candidate_service.create_candidate(request)
