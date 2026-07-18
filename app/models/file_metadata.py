from dataclasses import dataclass


@dataclass
class FileMetadata:
    path: str
    extension: str
    language: str
    size: int
    lines: int