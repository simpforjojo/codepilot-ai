from pathlib import Path
from git import Repo, GitCommandError
import shutil


class GitService:

    def clone(self, url: str, destination: Path):

        if destination.exists():
            shutil.rmtree(destination)

        try:
            Repo.clone_from(url, destination)
        except GitCommandError:
            raise Exception("Unable to clone the repository.")