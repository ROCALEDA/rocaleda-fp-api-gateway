from fastapi import APIRouter, Request

# from fastapi import Depends
# from app.commons.auth import validate_token

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

    # @router.get("/health")
    # async def authenticated_health(request: Request, _=Depends(validate_token)):
    #     print(request.state.user_data)
    #     print("Inside authenticated health")
    #     return "Ok"
