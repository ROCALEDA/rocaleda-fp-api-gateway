import httpx
from fastapi import Depends, Request, HTTPException

from app.commons.settings import settings
from app.commons.helpers import build_request_uri


def extract_token(request: Request) -> str:
    authorization: str = request.headers.get("Authorization")
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authentication token")
    return authorization.split(" ")[1]


async def validate_token(request: Request, token: str = Depends(extract_token)) -> bool:
    async with httpx.AsyncClient() as client:
        validation_url = (
            build_request_uri(settings.authentication_ms, "auth/validate/") + token
        )
        response = await client.get(validation_url)
        response_json = response.json()

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Unauthorized")

        request.state.user_data = response_json.get("data")

        return True
