# 🛡️ Portfólio de Cibersegurança: Engenharia de Segurança & Defesa Cibernética

Bem-vindo ao meu repositório focado em segurança ofensiva, defensiva e criptografia aplicada. Este espaço reúne projetos práticos desenvolvidos para demonstrar competências essenciais no ciclo de vida de desenvolvimento seguro (SDLC), automação de rotinas de monitoramento e mitigação de falhas críticas de segurança de software em conformidade com as principais metodologias globais (OWASP, MITRE ATT&CK).

---

## 🚀 Projetos Incluídos neste Repositório

### 1. 🔬 Analisador de Segurança & Prevenção a Estouro de Buffer (Buffer Overflow) em C
* *Arquivo Principal:* buffer_overflow.c
* *O que faz:* Estudo de caso prático que simula o tratamento seguro de entradas de dados em baixo nível. O projeto aborda a transição de funções inseguras do C padrão para práticas consolidadas de mitigação contra corrupção de memória.
* *Principais Conceitos Demonstrados:*
  * *Mitigação Prática de Buffer Overflow:* Substituição de métodos de leitura vulneráveis que não impõem limites à pilha pelo uso monitorado de fgets combinado ao operador sizeof.
  * *Tratamento Seguro de Strings:* Manipulação avançada e sanitização de buffers com remoção explícita de caracteres residuais de quebra de linha (\n), prevenindo comportamentos indefinidos no sistema.

### 2. 🔑 Engine de Criptografia Simétrica Avançada (AES-256-CBC) em Python
* *Arquivo Principal:* criptografia.py
* *O que faz:* Implementação de um módulo robusto de cifragem industrial utilizando o algoritmo AES com chaves de 256 bits no modo de operação Cipher Block Chaining (CBC). Garantia de confidencialidade de dados em repouso (Data at Rest).
* *Principais Conceitos Demonstrados:*
  * *Gerenciamento Seguro de Segredos:* Geração de Vetores de Inicialização (IV) e chaves mestras criptograficamente fortes através de entropia do sistema operacional (os.urandom).
  * *Alinhamento de Blocos (Padding):* Implementação do padrão PKCS7 para estruturação uniforme de dados simétricos antes do processamento de cifragem.

### 📊 3. Analisador Forense de Logs & Detecção de Ameaças (SIEM Script) em Python
* *Arquivo Principal:* analisador_logs.py
* *O que faz:* Script focado em operações de Defesa (Blue Team). Ele realiza a varredura sistemática e automatizada de logs de servidores web para identificar assinaturas conhecidas de ataques em tempo real.
* *Principais Conceitos Demonstrados:*
  * *Análise de Assinaturas com Regex:* Uso de expressões regulares avançadas para identificar tentativas de injeção de código e manipulação de caminhos de diretório.
  * *Identificação de Vetores de Ataque:* Detecção automatizada de vulnerabilidades críticas como SQL Injection (SQLi) e Path Traversal.

### ⚡ 4. Scanner de Portas de Rede Automatizado (Network Port Scanner) em Python
* *Arquivo Principal:* port_scanner.py
* *O que faz:* Um script em Python otimizado para realizar varreduras de segurança em ativos de redes locais. Ele analisa de maneira sistemática endereços IP para identificar portas de comunicação expostas a ameaças.
* *Principais Conceitos Demonstrados:*
  * *Redes e Protocolos:* Análise da integridade da comunicação utilizando arquiteturas TCP/IP e simulação das etapas do Three-Way Handshake.
  * *Fase de Reconhecimento (Footprinting):* Descoberta de vetores e superfícies de ataque em auditorias internas.

---

## 🛠️ Tecnologias e Ferramentas Empregadas
* *Linguagens de Programação:* C e Python
* *Bibliotecas Especializadas:* cryptography (hazmat primitives), re, socket
* *Frameworks e Metodologias:* OWASP Top 10, Práticas de Revisão de Código de Segurança (Secure Code Review)

---

## ⚙️ Como Executar e Testar os Projetos

### 🔹 Módulo de Criptografia (Python)
Certifique-se de instalar as dependências de criptografia padrão do mercado:
bash
pip install cryptography
python3 criptografia.py


### 🔹 Módulo de Análise de Logs (Python)
bash
python3 analisador_logs.py


### 🔹 Módulo de Varredura de Redes (Python)
bash
python3 port_scanner.py


### 🔹 Módulo de Prevenção a Overflow (C)
bash
gcc buffer_overflow.c -o buffer_overflow
./buffer_overflow
