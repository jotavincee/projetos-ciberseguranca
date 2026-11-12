
#!/usr/bin/env python3
"""
HONEYPOT SECURITY SIMULATOR
Cybersecurity | Threat Monitoring | Blue Team
"""

import argparse
import json
import socket

from datetime import datetime, timezone


def start_honeypot(host, port, log_file):

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((host, port))

    server.listen(10)

    print("\n=== HONEYPOT MONITORING ===")

    print(f"Listening on {host}:{port}")

    print("Press CTRL+C to stop.\n")

    try:

        while True:

            connection, address = server.accept()

            with connection:

                event = {

                    "timestamp": datetime.now(
                        timezone.utc
                    ).isoformat(),

                    "source_ip": address[0],

                    "source_port": address[1],

                    "destination_port": port,

                    "event": "connection_received"

                }

                with open(
                    log_file,
                    "a",
                    encoding="utf-8"
                ) as log:

                    log.write(
                        json.dumps(event) + "\n"
                    )

                print("[CONNECTION DETECTED]")

                print(
                    json.dumps(
                        event,
                        indent=4
                    )
                )

                connection.sendall(
                    b"Monitoring service active.\n"
                )

    finally:

        server.close()


def main():

    parser = argparse.ArgumentParser(
        description="Honeypot Security Simulator"
    )

    parser.add_argument(
        "--host",
        default="127.0.0.1"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=2222
    )

    parser.add_argument(
        "--log",
        default="honeypot_events.jsonl"
    )

    args = parser.parse_args()

    if not 1 <= args.port <= 65535:
        parser.error("Invalid port.")

    start_honeypot(
        args.host,
        args.port,
        args.log
    )


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nHoneypot stopped.")
