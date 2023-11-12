from fastapi import APIRouter, Request

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
