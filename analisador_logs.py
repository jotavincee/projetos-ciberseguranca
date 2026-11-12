
#!/usr/bin/env python3
"""
SECURITY LOG ANALYZER
Cybersecurity | Blue Team | Threat Detection
"""

import argparse
import re
from collections import Counter
from pathlib import Path

RULES = {
    "SQL Injection": r"union\s+select|or\s+['\"]?1['\"]?\s*=\s*['\"]?1",
    "Path Traversal": r"\.\./|%2e%2e%2f",
    "Brute Force Indicator": r"failed password|authentication failure|login failed|invalid password",
    "Sensitive File Access": r"/\.env|/etc/passwd|wp-config\.php",
    "Suspicious Scanner": r"nmap|masscan|zmap"
}

def analyze_logs(file_path):
    findings = []
    counters = Counter()

    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
        for line_number, line in enumerate(file, 1):

            for attack, pattern in RULES.items():

                if re.search(pattern, line, re.IGNORECASE):
                    findings.append({
                        "line": line_number,
                        "attack": attack,
                        "evidence": line.strip()
                    })

                    counters[attack] += 1

    return findings, counters


def main():

    parser = argparse.ArgumentParser(
        description="Security Log Analyzer"
    )

    parser.add_argument("arquivo", help="Arquivo de log")
    parser.add_argument("--saida", help="Arquivo para salvar relatório")

    args = parser.parse_args()

    path = Path(args.arquivo)

    if not path.is_file():
        parser.error("Arquivo não encontrado.")

    findings, counters = analyze_logs(path)

    print("\n=== SECURITY LOG ANALYZER ===\n")

    if not findings:
        print("Nenhum padrão suspeito identificado.")

    for item in findings:
        print(
            f"[ALERTA] Linha {item['line']} | "
            f"{item['attack']}"
        )
        print(f"Evidência: {item['evidence']}\n")

    print("=== RESUMO ===")

    for attack, total in counters.most_common():
        print(f"{attack}: {total}")

    print(f"\nTotal de ocorrências: {len(findings)}")

    if args.saida:
        with open(args.saida, "w", encoding="utf-8") as report:
            for item in findings:
                report.write(
                    f"{item['line']} | {item['attack']} | "
                    f"{item['evidence']}\n"
                )

        print(f"Relatório salvo em: {args.saida}")


if __name__ == "__main__":
    main()
