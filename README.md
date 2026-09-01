# 🛡️ Portfólio Avançado de Cibersegurança: Engenharia, Defesa & Arquitetura de Redes

Bem-vindo ao meu repositório avançado de engenharia de segurança cibernética. Este espaço reúne implementações profissionais focadas em segurança de aplicações (AppSec), criptografia aplicada à governança de dados, inteligência de ameaças (Cyber Threat Intelligence) e automação defensiva (Blue Team) alinhadas aos frameworks globais *OWASP Top 10, **MITRE ATT&CK* e melhores práticas do mercado corporativo.

---

## 🚀 Projetos Incluídos neste Repositório

### 1. 🔬 Analisador de Segurança & Prevenção a Estouro de Buffer (C)
* *Arquivo:* buffer_overflow.c
* *Escopo:* Mitigação de vulnerabilidades críticas em código legado em baixo nível através de sanitização da memória pilha utilizando fgets e controle de tamanho dinâmico por sizeof.

### 2. 🔑 Engine de Criptografia Simétrica Avançada (AES-256-CBC) (Python)
* *Arquivo:* criptografia.py
* *Escopo:* Implementação corporativa de criptografia simétrica para proteção de dados em repouso (Data at Rest). Utiliza derivação robusta de blocos com o padrão PKCS7 e vetores de inicialização por entropia segura (os.urandom).

### 📊 3. Analisador Forense de Logs & Detecção de Ameaças (SIEM Script) (Python)
* *Arquivo:* analisador_logs.py
* *Escopo:* Script voltado para SOC/Blue Team. Realiza varreduras automatizadas e análise por expressões regulares (Regex) em logs brutos de servidores para detectar assinaturas de ataques em tempo real, como SQLi e Path Traversal.

### ⚡ 4. Scanner de Portas de Rede Automatizado (Network Port Scanner) (Python)
* *Arquivo:* port_scanner.py
* *Escopo:* Scanner de ativos de infraestrutura de rede utilizando sockets nativos para mapear a exposição de portas TCP abertas na superfície externa da rede de computadores.

### 🛡️ 5. API Security Gateway, Rate Limiting & Proteção contra XSS (Python)
* *Arquivo:* api_security_gateway.py
* *Escopo:* Gateway defensivo com algoritmo de janela de tempo (Fixed Window) para mitigar de forma ativa ataques de força bruta, ataques DoS e injeções de scripts maliciosos (XSS) via sanitização de payloads HTML.

### 🗂️ 6. Monitor de Integridade de Arquivos Críticos - FIM (Python)
* *Arquivo:* verificador_integridade.py
* *Escopo:* Sistema preventivo contra Ransomwares e Rootkits. Gera uma linha de base criptográfica (Baseline) contendo o hash SHA-256 de diretórios críticos e monitora variações não autorizadas na integridade das estruturas de arquivos.

### 🛰️ 7. Analisador Forense Estrutural de Tráfego de Pacotes PCAP (Python)
* *Arquivo:* analisador_pcap.py
* *Escopo:* Decodificação de estruturas de cabeçalhos de pacotes IP e frames de baixo nível em formato binário bruto através do módulo struct. Essencial para investigações digitais e triagens de anomalias em tráfego de rede.

### 🔐 8. Secrets Vault & Derivador de Chaves Industriais (PBKDF2) (Python)
* *Arquivo:* gerenciador_segredos.py
* *Escopo:* Sistema gerenciador de credenciais que elimina o risco de exposição de senhas e tokens em código fonte. Aplica o robusto algoritmo KDF PBKDF2 com salt aleatório e criptografia autenticada Fernet.

### 🕸️ 9. Honeypot SSH Ativo de Decepção e Captura de Artefatos (Python)
* *Arquivo:* simulador_honeypot.py
* *Escopo:* Defesa ativa cibernética baseada em armadilhas de rede (Deception Technology). Cria um socket ouvinte falso simulando terminais SSH vulneráveis para coletar payloads de invasores, gerando inteligência e logs forenses detalhados.

---

## 🛠️ Tecnologias e Ferramentas Empregadas
* *Linguagens de Programação:* C (Baixo Nível/Segurança de Software) e Python 3 (Segurança de Automações)
* *Módulos Especializados:* cryptography, struct, socket, hashlib, re
* *Conceitos de Engenharia:* SDLC Seguro, Hardening, Gestão de Identidades (IAM), Forense Digital e Threat Hunting

---

## ⚙️ Instalação e Execução das Ferramentas do Portfólio

Para testar as automações em Python, instale as primitivas criptográficas recomendadas pelo ecossistema industrial:
bash
pip install cryptography


### Exemplo: Executando o Secrets Vault Corporativo
bash
python3 gerenciador_segredos.py


### Exemplo: Executando a Prevenção contra Buffer Overflow
bash
gcc buffer_overflow.c -o buffer_overflow
./buffer_overflow
