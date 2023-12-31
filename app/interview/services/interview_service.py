from fastapi import Request, HTTPException

from app.commons.auth import extract_token, validate_token
from app.interview.repositories.interview_repository import InterviewRepository


class InterviewService:
    def __init__(self, interview_repository: InterviewRepository):
        self.interview_repository = interview_repository

    async def get_candidates_paginated(self, request: Request):
        try:
            received_token = extract_token(request)
            await validate_token(request, received_token)
            return await self.interview_repository.get_interviews_paginated(
                str(request.state.user_data["role_id"]),
                str(request.state.user_data["user_id"]),
                request,
            )
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error")

    async def create_interview(self, request: Request):
        try:
            return await self.interview_repository.create_interview(request)
        except HTTPException as e:
            print("Http exception: ", e.detail)
            raise e
        except Exception as e:
            print("Internal server error: ", e)
            raise HTTPException(500, "Internal server error") from e
