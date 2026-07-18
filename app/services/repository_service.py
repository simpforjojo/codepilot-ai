from pathlib import Path

from app.services.file_service import FileService
from app.services.git_service import GitService
from app.services.code_reader import CodeReader

class RepositoryService:

    def __init__(self):
        self.git = GitService()
        self.files = FileService()
        self.repository_directory = Path("repositories")
        self.reader = CodeReader()

    def clone_repository(self, url: str):

        repo_name = url.rstrip("/").split("/")[-1]
        destination = self.repository_directory / repo_name

        if not destination.exists():
            self.git.clone(url, destination)

        files = self.files.scan(destination)
        codebase = self.reader.read(destination, files)
        return {
            "success": True,
            "repository": repo_name,
            "total_files": len(files),
            "codebase": codebase[:5]
        }
    def list_repositories(self):

        repositories = []

        if not self.repository_directory.exists():
            return repositories

        for folder in self.repository_directory.iterdir():

            if folder.is_dir():

                repositories.append(folder.name)

        return repositories