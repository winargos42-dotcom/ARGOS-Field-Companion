from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Protocol

class VisionBackend(Protocol):
    def describe(self, image: Path) -> str: ...

@dataclass(frozen=True)
class Observation:
    timestamp: str
    image: str
    description: str
    mission: str

def build_mission(description: str) -> str:
    text = description.strip()
    if not text:
        raise ValueError("description must not be empty")
    return f"Find one real-world detail related to: {text}. Observe it without disturbing wildlife or plants."

def observe(image: Path, backend: VisionBackend) -> Observation:
    if not image.is_file():
        raise FileNotFoundError(image)
    description = backend.describe(image).strip()
    if not description:
        raise ValueError("vision backend returned an empty description")
    return Observation(datetime.now(timezone.utc).isoformat(), str(image), description, build_mission(description))

def append_journal(entry: Observation, journal: Path) -> None:
    journal.parent.mkdir(parents=True, exist_ok=True)
    with journal.open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(entry), ensure_ascii=False) + "\n")
