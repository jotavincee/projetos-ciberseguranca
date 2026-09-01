import re


PADROES_DE_ATAQUE = {
    "SQL Injection": re.compile(r"(UNION\s+SELECT|SELECT\s+.*\s+FROM|'OR\s+'1'='1)", re.IGNORECASE),
    "Path Traversal": re.compile(r"(\.\./\.\./|\.\.\\\.\.\\)", re.IGNORECASE),
}

def analisar_linha_log(linha_do_log: str):
    """Varre linhas de logs do servidor web buscando assinaturas de ataques comuns."""
    for tipo_ataque, regex in PADROES_DE_ATAQUE.items():
        if regex.search(linha_do_log):
            return tipo_ataque
    return None

if _name_ == "_main_":
    
    logs_simulados = [
        '192.168.1.50 - - [01/Sep/2026:10:00:00] "GET /index.php?id=1 HTTP/1.1" 200 4502',
        '10.0.0.15 - - [01/Sep/2026:10:02:15] "GET /vulneravel.php?id=1%20UNION%20SELECT%20null,username,password%20FROM%20users HTTP/1.1" 500 230',
        '172.16.5.4 - - [01/Sep/2026:10:05:42] "GET /../../../../etc/passwd HTTP/1.1" 403 120'
    ]
    
    print("=== RELATÓRIO DE MONITORAMENTO DE LOGS (SIEM SCRIPT) ===")
    for linha in logs_simulados:
        alerta = analisar_linha_log(linha)
        if alerta:
            print(f"[ALERTA CRÍTICO] Tentativa de {alerta} detectada na linha:\n -> {linha}\n")
