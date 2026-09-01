import struct

def analisar_pacote_falso(dados_pacote: bytes):
    """Decodifica um cabeçalho IP simulado estruturado em bytes de baixo nível."""
    print("=== ANÁLISE FORENSE DE PACOTE DE REDE (BYTES) ===")
    try:
        
        cabecalho = struct.unpack("!BBHHHBBH4s4s", dados_pacote[:20])
        ttl = cabecalho[5]
        protocolo = cabecalho[6]
        ip_origem = ".".join(map(str, cabecalho[8]))
        ip_destino = ".".join(map(str, cabecalho[9]))
        
        print(f"Origem: {ip_origem} -> Destino: {ip_destino}")
        print(f"TTL: {ttl} | Protocolo do Pacote: {protocolo}")
        
        if protocolo == 6:
            print("[INFO] Protocolo TCP identificado. Analisando payloads...")
        elif protocolo == 17:
            print("[INFO] Protocolo UDP identificado.")
            
    except Exception as e:
        print(f"[-] Falha na decodificação estrutural do pacote: {e}")

if _name_ == "_main_":
    
    pacote_raw_exemplo = b'E\x00\x00( \xbf\x00\x00@\x06\xfa\x83\xc0\xa8\x01\x01\n\x00\x00\x01'
    analisar_pacote_falso(pacote_raw_exemplo)
