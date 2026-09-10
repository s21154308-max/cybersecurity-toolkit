"""Display basic components of a URL."""

from urllib.parse import urlparse


def main() -> None:
    print("🔗 URL Analyzer")
    raw_url = input("Enter a URL: ").strip()

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


if __name__ == "__main__":
    main()
