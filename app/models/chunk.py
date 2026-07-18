from dataclasses import dataclass

@dataclass
class Chunk:
    id: str
    file_path: str
    content: str
    start_line: int
    end_line: int