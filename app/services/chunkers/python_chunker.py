from pathlib import Path
import ast
from app.models.chunk import Chunk
from app.services.chunkers.chunk_strategy import ChunkStrategy


class PythonChunker(ChunkStrategy):

    def chunk(self, path: Path) -> list[Chunk]:

        source = path.read_text(encoding="utf-8")

        tree = ast.parse(source)

        lines = source.splitlines()

        chunks = []

        for node in ast.walk(tree):

            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

                start = node.lineno
                end = node.end_lineno

                content = "\n".join(lines[start - 1:end])

                chunks.append(
                    Chunk(
                        id=f"{path}:{node.name}",
                        file_path=str(path),
                        content=content,
                        start_line=start,
                        end_line=end
                    )
                )

        return chunks