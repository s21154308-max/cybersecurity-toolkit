"""Interactive command-line menu for the Cybersecurity Toolkit."""

from tools.file_hash import sha256_file
from tools.password_checker import check_password
from tools.port_scanner import scan_port, COMMON_PORTS
from tools.url_analyzer import urlparse
import getpass\nimport socket


def password_checker() -> None:
    password = input("\nEnter a password to evaluate: ")
    score, feedback = check_password(password)

    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    print(f"\nScore: {score}/6")
    print(f"Rating: {rating}")

    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("The password meets all basic checks.")


def file_hash_generator() -> None:
    file_path = input("\nEnter the path of a local file: ").strip()

    try:
        print(f"\nSHA-256: {sha256_file(file_path)}")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except OSError as exc:
        print(f"Error reading file: {exc}")


def port_scanner() -> None:
    print("\nUse this only on a host you own or are explicitly authorized to test.")
    host = input("Enter an authorized hostname or IP address: ").strip()

    if not host:
        print("Error: Host cannot be empty.")
        return

    try:
        resolved = socket.gethostbyname(host)
        print(f"\nScanning {host} ({resolved})...")

        for port in COMMON_PORTS:
            status = "OPEN" if scan_port(resolved, port) else "CLOSED"
            print(f"[{status:<6}] TCP {port}")
    except socket.gaierror:
        print("Error: Could not resolve the host.")


def url_analyzer() -> None:
    raw_url = input("\nEnter a URL: ").strip()

    if not raw_url:
        print("Error: URL cannot be empty.")
        return

    if "://" not in raw_url:
        raw_url = "https://" + raw_url

    parsed = urlparse(raw_url)

    print("\nURL Components")
    print(f"Scheme:   {parsed.scheme or 'N/A'}")
    print(f"Domain:   {parsed.hostname or 'N/A'}")
    print(f"Port:     {parsed.port or 'Default'}")
    print(f"Path:     {parsed.path or '/'}")
    print(f"Query:    {parsed.query or 'N/A'}")
    print(f"Fragment: {parsed.fragment or 'N/A'}")


def pause() -> None:\n    input("\nPress Enter to return to the menu...")\n\n\ndef show_menu() -> None:
    print("\n" + "=" * 42)
    print("        🔐 CYBERSECURITY TOOLKIT")
    print("=" * 42)
    print("1. Password Strength Checker")
    print("2. SHA-256 File Hash Generator")
    print("3. TCP Port Scanner")
    print("4. URL Analyzer")
    print("5. Exit")
    print("=" * 42)


def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            password_checker()
        elif choice == "2":
            file_hash_generator()
        elif choice == "3":
            port_scanner()
        elif choice == "4":
            url_analyzer()
        elif choice == "5":
            print("\nExiting Cybersecurity Toolkit. Stay ethical! 🛡️")
            break
        else:
            print("\nInvalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
