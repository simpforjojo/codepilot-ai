from fastapi import FastAPI

from app.api.repositories import router as repositories_router

app = FastAPI(
    title="CodePilot AI",
    version="1.0.0"
)

app.include_router(repositories_router)


@app.get("/")
def health():
    return {
        "status": "running"
    }