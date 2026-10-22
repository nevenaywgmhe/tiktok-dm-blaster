from pathlib import Path
import json


def read_lines(path: Path) -> list[str]:
    return [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def append_report(path: Path, entry: dict) -> None:
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry) + "\n")