import hashlib
import os
import json

def calcular_sha256(caminho_arquivo: str) -> str:
    """Gera o hash SHA-256 de um arquivo de forma eficiente usando blocos."""
    sha256 = hashlib.sha256()
    try:
        with open(caminho_arquivo, "rb") as f:
            while bloco := f.read(4096):
                sha256.update(bloco)
        return sha256.hexdigest()
    except FileNotFoundError:
        return ""

def gerar_baseline(diretorio: str, arquivo_banco: str):
    """Cria uma foto do estado original dos hashes dos arquivos (Baseline)."""
    banco_dados = {}
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            banco_dados[caminho_completo] = calcular_sha256(caminho_completo)
            
    with open(arquivo_banco, "w") as f:
        json.dump(banco_dados, f, indent=4)
    print(f"[+] Baseline gerada com sucesso em {arquivo_banco}")

def verificar_integridade(arquivo_banco: str):
    """Compara os hashes atuais com a baseline para detectar adulterações."""
    if not os.path.exists(arquivo_banco):
        print("[-] Erro: Arquivo de baseline não encontrado.")
        return

    with open(arquivo_banco, "r") as f:
        baseline = json.load(f)

    print("\n=== AUDITORIA DE INTEGRIDADE EM ANDAMENTO ===")
    for caminho, hash_original in baseline.items():
        if not os.path.exists(caminho):
            print(f"[ALERTA CRÍTICO] Arquivo DELETADO ou REMOVIDO: {caminho}")
            continue
            
        hash_atual = calcular_sha256(caminho)
        if hash_atual != hash_original:
            print(f"[ALERTA CRÍTICO] Arquivo MODIFICADO ilegalmente: {caminho}")
            print(f" -> Hash Original: {hash_original}")
            print(f" -> Hash Atual:    {hash_atual}")
        else:
            print(f"[OK] Arquivo íntegro: {caminho}")

if _name_ == "_main_":
    
    os.makedirs("./arquivos_criticos", exist_ok=True)
    with open("./arquivos_criticos/config.sys", "w") as f: f.write("ALLOW_ACCESS=FALSE")
    
    
    gerar_baseline("./arquivos_criticos", "baseline.json")
    
    
    with open("./arquivos_criticos/config.sys", "w") as f: f.write("ALLOW_ACCESS=TRUE")
    
    
    verificar_integridade("baseline.json")
