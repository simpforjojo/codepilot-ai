from abc import ABC, abstractmethod
from pathlib import Path
from app.models.chunk import Chunk

class ChunkStrategy(ABC):

    @abstractmethod
    def chunk(self, path: Path) -> list[Chunk]:
        pass