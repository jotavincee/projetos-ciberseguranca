import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import os

class SecretsManager:
    def _init_(self, senha_mestra: str):
        
        self.salt = os.urandom(16)
        
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        chave_derivada = base64.urlsafe_b64encode(kdf.derive(senha_mestra.encode()))
        self.fernet = Fernet(chave_derivada)

    def guardar_credencial(self, secret_chave: str) -> bytes:
        """Criptografa e blinda uma credencial."""
        return self.fernet.encrypt(secret_chave.encode())

    def ler_credencial(self, token_criptografado: bytes) -> str:
        """Descriptografa o segredo em memória."""
        return self.fernet.decrypt(token_criptografado).decode()

if _name_ == "_main_":
    print("=== VAULT DE CREDENCIAIS CORPORATIVO ===")
    MINHA_SENHA_INFRA = "SenhaMestraSegura#2026"
    
    vault = SecretsManager(MINHA_SENHA_INFRA)
    
    
    string_conexao_db = "postgresql://admin:SenhaSuperSecretaDoProducao@10.0.0.5:5432/db"
    
    secreto_protegido = vault.guardar_credencial(string_conexao_db)
    print(f"[PROTEGIDO] String criptografada gravada: {secreto_protegido[:50]}...")
    
    descriptografado = vault.ler_credencial(secreto_protegido)
    print(f"[MEMÓRIA] Dado recuperado com sucesso para conexão segura.")
