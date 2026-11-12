
#!/usr/bin/env python3
"""
API SECURITY GATEWAY
Application Security | API Protection
"""

import os
import time

from collections import defaultdict, deque
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Enterprise API Security Gateway",
    description="Educational API security gateway",
    version="1.0.0"
)

API_TOKEN = os.getenv("API_TOKEN", "change-me")
MAX_REQUESTS = int(os.getenv("MAX_REQUESTS_PER_MINUTE", "60"))

requests_by_ip = defaultdict(deque)


@app.middleware("http")
async def security_middleware(request: Request, call_next):

    current_time = time.time()

    client_ip = (
        request.client.host
        if request.client
        else "unknown"
    )

    request_history = requests_by_ip[client_ip]

    while request_history and current_time - request_history[0] > 60:
        request_history.popleft()

    if len(request_history) >= MAX_REQUESTS:

        return JSONResponse(
            status_code=429,
            content={
                "error": "Rate limit exceeded",
                "message": "Too many requests"
            }
        )

    request_history.append(current_time)

    response = await call_next(request)

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Cache-Control"] = "no-store"

    return response


@app.get("/")
def home():

    return {
        "service": "API Security Gateway",
        "status": "operational"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.get("/private")
def protected_endpoint(request: Request):

    supplied_token = request.headers.get("X-API-Key")

    if not supplied_token or supplied_token != API_TOKEN:

        raise HTTPException(
            status_code=401,
            detail="Unauthorized access"
        )

    return {
        "message": "Authenticated successfully",
        "access": "granted"
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
