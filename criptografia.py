import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def criptografar_dados(dados: bytes, chave: bytes) -> tuple[bytes, bytes]:
    """Criptografa dados usando AES-256 no modo CBC com preenchimento PKCS7."""
    
    iv = os.urandom(16)
    
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    dados_preenchidos = padder.update(dados) + padder.finalize()
    
    
    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    texto_criptografado = encryptor.update(dados_preenchidos) + encryptor.finalize()
    return iv, texto_criptografado

if _name_ == "_main_":
    
    CHAVE_MESTRA = os.urandom(32)
    mensagem_secreta = b"Dados confidenciais de credenciais de usuarios."
    
    iv, criptografado = criptografar_dados(mensagem_secreta, CHAVE_MESTRA)
    
    print("=== MÓDULO DE CRIPTOGRAFIA AES-256 ===")
    print(f"IV (Hex): {iv.hex()}")
    print(f"Resultado Criptografado (Hex): {criptografado.hex()}")
