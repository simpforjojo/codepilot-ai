from pathlib import Path


class FileService:

    SUPPORTED_EXTENSIONS = {
        ".py",
        ".js",
        ".ts",
        ".java",
        ".cpp",
        ".c",
        ".cs",
        ".go",
        ".rs",
        ".html",
        ".css",
        ".json",
        ".md",
        ".yaml",
        ".yml",
    }

    IGNORED_DIRECTORIES = {
        ".git",
        "__pycache__",
        "node_modules",
        ".venv",
        "venv",
    }

    def scan(self, repository_path: Path):

        files = []

        for file in repository_path.rglob("*"):

            if any(folder in self.IGNORED_DIRECTORIES for folder in file.parts):
                continue

            if file.is_file() and file.suffix in self.SUPPORTED_EXTENSIONS:
                files.append(str(file.relative_to(repository_path)))

        return files