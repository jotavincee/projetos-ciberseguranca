import socket
import datetime

def iniciar_honeypot_ssh(host: str = "0.0.0.0", porta: int = 2222):
    """Inicia um serviço SSH simulado na porta 2222 para monitorar engenharia reversa."""
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        servidor.bind((host, porta))
        servidor.listen(5)
        print(f"[*] Honeypot de Armadilha SSH ativo ouvindo na porta {porta}...")
        
        
        cliente, endereco = servidor.accept()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[ALERTA DE INTRUSÃO] Conexão suspeita vinda de {endereco[0]}:{endereco[1]} em {timestamp}")
        
        
        cliente.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n")
        dados_recebidos = cliente.recv(1024)
        
        print(f"[LOG FORENSE] Dados de payload inseridos pelo atacante: {dados_recebidos}")
        cliente.close()
        
    except KeyboardInterrupt:
        print("\n[-] Honeypot encerrado pelo operador.")
    except Exception as e:
        print(f"[-] Erro operacional na execução do Socket: {e}")
    finally:
        servidor.close()

if _name_ == "_main_":
    
    iniciar_honeypot_ssh()
