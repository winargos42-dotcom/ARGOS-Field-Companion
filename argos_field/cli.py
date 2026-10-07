import argparse
from pathlib import Path
from .backends import DemoBackend
from .core import append_journal, observe

def main() -> None:
    p = argparse.ArgumentParser(description="ARGOS Field Companion")
    p.add_argument("image", type=Path)
    p.add_argument("--journal", type=Path, default=Path("field-journal.jsonl"))
    args = p.parse_args()
    entry = observe(args.image, DemoBackend())
    append_journal(entry, args.journal)
    print(entry.description)
    print("MISSION:", entry.mission)

if __name__ == "__main__":
    main()
