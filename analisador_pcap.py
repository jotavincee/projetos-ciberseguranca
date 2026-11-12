
#!/usr/bin/env python3
"""
NETWORK TRAFFIC ANALYZER
Cybersecurity | Network Security
"""

import argparse
from collections import Counter
from scapy.all import rdpcap, IP, TCP, UDP, DNS, DNSQR


def analyze_pcap(file_path):

    packets = rdpcap(file_path)

    protocols = Counter()
    sources = Counter()
    destinations = Counter()
    ports = Counter()
    dns_queries = []

    for packet in packets:

        if IP in packet:

            ip = packet[IP]

            sources[ip.src] += 1
            destinations[ip.dst] += 1

            if TCP in packet:
                protocols["TCP"] += 1
                ports[packet[TCP].dport] += 1

            elif UDP in packet:
                protocols["UDP"] += 1
                ports[packet[UDP].dport] += 1

            else:
                protocols["IP/Other"] += 1

        if DNS in packet and packet[DNS].qd and DNSQR in packet:

            query = packet[DNSQR].qname.decode(
                errors="replace"
            )

            dns_queries.append(query)

    return (
        len(packets),
        protocols,
        sources,
        destinations,
        ports,
        dns_queries
    )


def main():

    parser = argparse.ArgumentParser(
        description="Network Traffic Analyzer"
    )

    parser.add_argument("pcap", help="Arquivo PCAP")

    args = parser.parse_args()

    results = analyze_pcap(args.pcap)

    total, protocols, sources, destinations, ports, dns = results

    print("\n=== NETWORK TRAFFIC ANALYZER ===")

    print(f"\nTotal de pacotes: {total}")

    print("\nProtocolos:")
    for protocol, count in protocols.most_common():
        print(f"{protocol}: {count}")

    print("\nPrincipais IPs de origem:")
    for ip, count in sources.most_common(10):
        print(f"{ip}: {count} pacotes")

    print("\nPrincipais IPs de destino:")
    for ip, count in destinations.most_common(10):
        print(f"{ip}: {count} pacotes")

    print("\nPortas de destino:")
    for port, count in ports.most_common(10):
        print(f"Porta {port}: {count} pacotes")

    print("\nConsultas DNS:")
    for query in dns[:20]:
        print(query)


if __name__ == "__main__":
    main()
