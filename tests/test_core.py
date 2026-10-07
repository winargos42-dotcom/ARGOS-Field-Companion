import json
from pathlib import Path
import pytest
from argos_field.core import append_journal, build_mission, observe

class FakeVision:
    def describe(self, image: Path) -> str:
        return "a moss-covered tree trunk"

def test_observe_and_journal(tmp_path):
    image = tmp_path / "tree.jpg"
    image.write_bytes(b"test-image")
    entry = observe(image, FakeVision())
    assert entry.description == "a moss-covered tree trunk"
    assert "real-world detail" in entry.mission
    journal = tmp_path / "journal.jsonl"
    append_journal(entry, journal)
    row = json.loads(journal.read_text())
    assert row["description"] == entry.description
    assert row["image"].endswith("tree.jpg")

def test_missing_image_fails(tmp_path):
    with pytest.raises(FileNotFoundError):
        observe(tmp_path / "missing.jpg", FakeVision())

def test_empty_description_fails(tmp_path):
    image = tmp_path / "x.jpg"
    image.write_bytes(b"x")
    class Empty:
        def describe(self, image): return " "
    with pytest.raises(ValueError):
        observe(image, Empty())

def test_mission_rejects_empty():
    with pytest.raises(ValueError):
        build_mission(" ")
