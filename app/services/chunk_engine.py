from pathlib import Path
from app.models.chunk import Chunk
from app.services.chunkers.python_chunker import PythonChunker
from app.services.chunkers.chunk_strategy import ChunkStrategy


class ChunkEngine:

    def __init__(self):
        self.strategies: dict[str, ChunkStrategy] = {
            ".py": PythonChunker(),
        }

    def chunk(self, path: Path) -> list[Chunk]:

        strategy = self.strategies.get(path.suffix)

        if strategy is None:
            return []

        return strategy.chunk(path)