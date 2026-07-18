from fastapi import APIRouter, HTTPException

from app.schemas.repository import RepositoryRequest
from app.schemas.repository_response import RepositoryResponse
from app.services.repository_service import RepositoryService

router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"]
)

service = RepositoryService()


@router.post("", response_model=RepositoryResponse)
def clone_repository(request: RepositoryRequest):

    try:
        result = service.clone_repository(str(request.url))
        return result

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
@router.get("")
def list_repositories():

    return service.list_repositories()