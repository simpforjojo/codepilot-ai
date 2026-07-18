from pydantic import BaseModel


class RepositoryResponse(BaseModel):
    success: bool
    repository: str
    total_files: int