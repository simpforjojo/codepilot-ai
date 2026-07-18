from pathlib import Path


class CodeReader:

    def read(self, repository_path: Path, files: list[str]):

        codebase = []

        for file in files:

            path = repository_path / file

            try:
                content = path.read_text(encoding="utf-8")
            except Exception:
                continue

            codebase.append(
                {
                    "path": file,
                    "content": content
                }
            )

        return codebase