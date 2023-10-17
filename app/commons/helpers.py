def build_request_uri(host: str, endpoint: str) -> str:
    # TODO: Change to https
    return f"http://{host}/{endpoint}"
