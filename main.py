import re
import sys
from dataclasses import dataclass
from pathlib import Path
from collections import Counter


LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    r"\s+(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)"
    r"\s+(?P<module>\w+)"
    r"\s+(?P<message>.+)"
)


@dataclass
class LogEntry:
    timestamp: str
    level: str
    module: str
    message: str


def parse_line(line: str) -> LogEntry | None:
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None
    return LogEntry(**match.groupdict())


def parse_file(path: Path) -> list[LogEntry]:
    entries: list[LogEntry] = []
    with path.open() as f:
        for line in f:
            entry = parse_line(line)
            if entry:
                entries.append(entry)
    return entries


def summarize(entries: list[LogEntry]) -> None:
    levels = Counter(e.level for e in entries)
    print(f"Parsed {len(entries)} log entries\n")
    print("Level counts:")
    for level in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
        if level in levels:
            print(f"  {level}: {levels[level]}")
    print()
    errors = [e for e in entries if e.level in ("ERROR", "CRITICAL")]
    if errors:
        print("Errors:")
        for e in errors:
            print(f"  [{e.timestamp}] {e.module}: {e.message}")


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <logfile>")
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)
    entries = parse_file(path)
    summarize(entries)


if __name__ == "__main__":
    main()
