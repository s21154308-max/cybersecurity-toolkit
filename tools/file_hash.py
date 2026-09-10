"""Generate a SHA-256 hash for a local file."""

import hashlib
from pathlib import Path


def sha256_file(file_path: str) -> str:
    path = Path(file_path)
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)

    return digest.hexdigest()


def main() -> None:
    print("#️⃣ SHA-256 File Hash Generator")
    file_path = input("Enter the path of a local file: ").strip()

    try:
        print(f"\nSHA-256: {sha256_file(file_path)}")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except OSError as exc:
        print(f"Error reading file: {exc}")


if __name__ == "__main__":
    main()
