from pathlib import Path

from app.models.file_metadata import FileMetadata
from app.services.chunk_engine import ChunkEngine

class IndexService:

    LANGUAGE_MAP = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C",
        ".cs": "C#",
        ".go": "Go",
        ".rs": "Rust",
        ".html": "HTML",
        ".css": "CSS",
        ".json": "JSON",
        ".md": "Markdown",
        ".yaml": "YAML",
        ".yml": "YAML"
    }

    def build(self, repository_path: Path, files: list[str]):

        index = []

        for file in files:

            path = repository_path / file

            try:
                text = path.read_text(encoding="utf-8")
            except Exception:
                continue

            metadata = FileMetadata(
                path=file,
                extension=path.suffix,
                language=self.LANGUAGE_MAP.get(path.suffix, "Unknown"),
                size=path.stat().st_size,
                lines=len(text.splitlines())
            chunks = self.chunk_engine.chunk(path)
            )

            index.append(metadata)

        return index