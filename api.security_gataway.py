import time
from collections import defaultdict
import html

class APISecurityGateway:
    def _init_(self, limit: int, window_seconds: int):
        self.limit = limit
        self.window_seconds = window_seconds
        
        self.request_history = defaultdict(list)

    def is_rate_limited(self, ip_address: str) -> bool:
        """Aplica o algoritmo de Fixed Window para mitigar força bruta e DoS."""
        current_time = time.time()
        
        self.request_history[ip_address] = [
            t for t in self.request_history[ip_address] 
            if current_time - t < self.window_seconds
        ]
        
        if len(self.request_history[ip_address]) >= self.limit:
            return True
            
        self.request_history[ip_address].append(current_time)
        return False

    def sanitize_input(self, payload: str) -> str:
        """Sanitiza payloads para prevenir ataques de Cross-Site Scripting (XSS)."""
        return html.escape(payload)

if _name_ == "_main_":
    
    gateway = APISecurityGateway(limit=3, window_seconds=5)
    ip_teste = "192.168.1.100"
    
    print("=== SECURITY GATEWAY: SIMULAÇÃO DE TAXA DE REQUISIÇÃO ===")
    for i in range(1, 6):
        payload_vulneravel = "<script>alert('XSS')</script>"
        sanitizado = gateway.sanitize_input(payload_vulneravel)
        
        if gateway.is_rate_limited(ip_teste):
            print(f"[BLOQUEADO] Requisição {i} do IP {ip_teste} excedeu o limite. Payload Sanitizado: {sanitizado}")
        else:
            print(f"[PERMITIDO] Requisição {i} processada com sucesso. Payload Sanitizado: {sanitizado}")
        time.sleep(0.5)
