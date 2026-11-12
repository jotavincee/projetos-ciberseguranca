
#!/usr/bin/env python3
"""
NETWORK PORT SCANNER
Network Security | Defensive Reconnaissance
"""

import argparse
import socket

from concurrent.futures import ThreadPoolExecutor


def scan_port(host, port, timeout):

    try:

        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as connection:

            connection.settimeout(timeout)

            result = connection.connect_ex(
                (host, port)
            )

            if result == 0:
                return port

    except OSError:
        pass

    return None


def main():

    parser = argparse.ArgumentParser(
        description="Network Port Scanner"
    )

    parser.add_argument("host")

    parser.add_argument(
        "--start",
        type=int,
        default=1
    )

    parser.add_argument(
        "--end",
        type=int,
        default=1024
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=0.5
    )

    args = parser.parse_args()

    if not 1 <= args.start <= args.end <= 65535:
        parser.error("Invalid port range.")

    print("\n=== NETWORK PORT SCANNER ===")

    print(f"Target: {args.host}")

    print(
        f"Port range: {args.start}-{args.end}"
    )

    print("\nScanning...\n")

    with ThreadPoolExecutor(
        max_workers=100
    ) as executor:

        results = executor.map(
            lambda port: scan_port(
                args.host,
                port,
                args.timeout
            ),
            range(args.start, args.end + 1)
        )

    opened_ports = sorted(
        port for port in results
        if port is not None
    )

    print("=== RESULTS ===")

    if opened_ports:

        for port in opened_ports:

            print(
                f"[OPEN] TCP port {port}"
            )

    else:

        print("No open TCP ports identified.")

    print(
        f"\nTotal open ports: {len(opened_ports)}"
    )


if __name__ == "__main__":
    main()
