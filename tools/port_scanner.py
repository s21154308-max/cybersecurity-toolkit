"""Simple TCP connect scanner for authorized hosts only."""

import socket

COMMON_PORTS = [21, 22, 25, 53, 80, 110, 143, 443, 3306, 8080]


def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0


def main() -> None:
    print("🌐 Local TCP Port Scanner")
    print("Use this only on a host you own or are explicitly authorized to test.\n")

    host = input("Enter an authorized hostname or IP address: ").strip()
    if not host:
        print("Error: Host cannot be empty.")
        return

    try:
        resolved = socket.gethostbyname(host)
        print(f"Scanning {host} ({resolved})...\n")
    except socket.gaierror:
        print("Error: Could not resolve the host.")
        return

    for port in COMMON_PORTS:
        if scan_port(resolved, port):
            print(f"[OPEN]   TCP {port}")
        else:
            print(f"[CLOSED] TCP {port}")


if __name__ == "__main__":
    main()
