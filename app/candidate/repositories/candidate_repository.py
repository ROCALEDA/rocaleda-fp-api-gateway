import httpx
from fastapi import Request
from fastapi import HTTPException

from app.commons.settings import settings


class CandidateRepository:
    async def create_candidate(self, request: Request):
        async with httpx.AsyncClient() as client:
            try:
                body = await request.json()
                uri = self.__build_request_uri(settings.users_ms, "user/candidate/")
                print(f"Sending {body} to {uri}")
                response = await client.post(uri, json=body, timeout=60)

                if 400 <= response.status_code < 600:
                    raise HTTPException(
                        status_code=response.status_code, detail=response.text
                    )
                print(f"response {response}")
                return response.json()
            except Exception as e:
                print("Error on url call: ", e)
                raise HTTPException(
                    status_code=500,
                    detail="Internal Server Error",
                )

    def __build_request_uri(self, host: str, endpoint: str) -> str:
        return f"https://{host}/{endpoint}"
