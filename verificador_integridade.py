
#!/usr/bin/env python3
"""
FILE INTEGRITY MONITOR
Cybersecurity | File System Security
"""

import argparse
import hashlib
import json

from pathlib import Path


DATABASE = Path("integrity_baseline.json")


def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        for chunk in iter(
            lambda: file.read(4096),
            b""
        ):

            sha256.update(chunk)

    return sha256.hexdigest()


def scan_directory(target):

    files = (
        [target]
        if target.is_file()
        else [
            file
            for file in target.rglob("*")
            if file.is_file()
        ]
    )

    results = {}

    for file in files:

        results[str(file.resolve())] = calculate_hash(
            file
        )

    return results


def main():

    parser = argparse.ArgumentParser(
        description="File Integrity Monitor"
    )

    parser.add_argument("path")

    parser.add_argument(
        "--init",
        action="store_true",
        help="Create a new baseline"
    )

    args = parser.parse_args()

    target = Path(args.path)

    if not target.exists():
        parser.error("Target not found.")

    current = scan_directory(target)

    if args.init or not DATABASE.exists():

        DATABASE.write_text(
            json.dumps(
                current,
                indent=4
            ),
            encoding="utf-8"
        )

        print("Baseline successfully created.")

        print(
            f"Monitored files: {len(current)}"
        )

        return

    previous = json.loads(
        DATABASE.read_text(
            encoding="utf-8"
        )
    )

    print("\n=== FILE INTEGRITY REPORT ===\n")

    for file in sorted(
        set(previous) | set(current)
    ):

        if file not in previous:

            print(f"[NEW FILE] {file}")

        elif file not in current:

            print(f"[REMOVED] {file}")

        elif previous[file] != current[file]:

            print(f"[MODIFIED] {file}")

        else:

            print(f"[OK] {file}")

    print("\nIntegrity analysis completed.")


if __name__ == "__main__":
    main()
