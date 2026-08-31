import socket
import sys


alvo = "127.0.0.1"

print(f"Iniciando varredura de segurança no alvo: {alvo}")
print("-" * 50)

portas_comuns = [21, 22, 80, 443, 8080]

for porta in portas_comuns:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    
    resultado = s.connect_ex((alvo, porta))
    if resultado == 0:
        print(f" Alerta: Porta {porta} está ABERTA e exposta.")
    else:
        print(f"Porta {porta}: Fechada/Protegida.")
    s.close()
