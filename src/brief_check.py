"""Report unanswered questions in a Mygit project brief."""
import argparse
import sys
from pathlib import Path

DEFAULT_BRIEF = Path(__file__).resolve().parent.parent / "docs" / "project-brief.md"


def missing_decisions(text: str) -> list[str]:
    missing = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("|"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) == 2 and cells[1].lower().startswith("to decide"):
                missing.append(cells[0])
        elif line.startswith("- **") and ":**" in line:
            label, answer = line[4:].split(":**", 1)
            if answer.strip().lower().startswith("to decide"):
                missing.append(label)
    return missing


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Check which project brief decisions are still open.")
    parser.add_argument("brief", nargs="?", type=Path, default=DEFAULT_BRIEF, help="brief file (default: docs/project-brief.md)")
    args = parser.parse_args(argv)
    try:
        text = args.brief.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"Cannot read brief: {exc}", file=sys.stderr)
        return 2
    missing = missing_decisions(text)
    if missing:
        print("Decisions still needed:")
        for item in missing:
            print(f"- {item}")
        return 1
    print("No 'To decide' placeholders found in brief fields.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
