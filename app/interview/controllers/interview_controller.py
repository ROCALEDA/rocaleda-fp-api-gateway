from fastapi import APIRouter, Depends, Request
from app.commons.auth import validate_token

from app.interview.services.interview_service import InterviewService

router = APIRouter(
    prefix="/interviews",
    tags=["interviews"],
    responses={404: {"description": "Not found"}},
)


def initialize(interview_service: InterviewService):
    @router.get("")
    async def get_interviews(request: Request):
        return await interview_service.get_candidates_paginated(request)

    @router.post("")
    async def create_interview(request: Request, _=Depends(validate_token)):
        return await interview_service.create_interview(request)
