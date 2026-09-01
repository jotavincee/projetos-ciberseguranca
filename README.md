# 🛡️ Portfólio de Cibersegurança: Desenvolvimento Seguro & Análise de Vulnerabilidades

Bem-vindo ao meu repositório focado em segurança ofensiva e defensiva. Este espaço reúne projetos práticos desenvolvidos para demonstrar competências essenciais no ciclo de vida de desenvolvimento seguro (SDLC), automação de rotinas de infraestrutura e mitigação de falhas críticas de segurança de software em conformidade com as principais metodologias globais (OWASP, MITRE ATT&CK).

---

## 🚀 Projetos Incluídos neste Repositório

### 1. 🔬 Analisador de Segurança & Prevenção a Estouro de Buffer (Buffer Overflow) em C
* *Arquivo Principal:* busca_linear.c (Recomenda-se renomear futuramente para buffer_overflow.c)
* *O que faz:* Estudo de caso prático que simula o tratamento seguro de entradas de dados em baixo nível. O projeto aborda a transição de funções inseguras do C padrão para práticas consolidadas de mitigação contra corrupção de memória.
* *Principais Conceitos Demonstrados:*
  * *Mitigação Prática de Buffer Overflow:* Substituição de métodos de leitura vulneráveis que não impõem limites à pilha pelo uso monitorado de fgets combinado ao operador sizeof.
  * *Tratamento Seguro de Strings:* Manipulação avançada e sanitização de buffers com remoção explícita de caracteres residuais de quebra de linha (\n), prevenindo comportamentos indefinidos no sistema.
  * *Alinhamento com OWASP Top 10:* Aplicação direta de técnicas focadas no controle de integridade da memória e gerenciamento seguro de recursos em camadas próximas ao hardware.

### 2. ⚡ Scanner de Portas de Rede Automatizado (Network Port Scanner) em Python
* *Arquivo Principal:* teste1.py (Recomenda-se renomear futuramente para port_scanner.py)
* *O que faz:* Um script em Python otimizado para realizar varreduras de segurança em ativos de redes locais. Ele analisa de maneira sistemática endereços IP para identificar portas de comunicação e serviços críticos abertos expostos a explorações externas.
* *Principais Conceitos Demonstrados:*
  * *Redes e Protocolos:* Análise da integridade da comunicação utilizando arquiteturas TCP/IP e simulação conceitual das etapas do Three-Way Handshake.
  * *Fase de Reconhecimento (Footprinting):* Simulação de técnicas legítimas e automatizadas para descoberta superficial de vetores e superfícies de ataque em auditorias internas.
  * *Automação Ofensiva/Defensiva:* Desenvolvimento de soluções rápidas com módulos nativos de Python voltados à agilização de tarefas manuais de triagem para equipes de segurança.

---

## 🛠️ Tecnologias e Ferramentas Empregadas
* *Linguagens de Programação:* C e Python
* *Metodologias e Frameworks:* Práticas de Revisão de Código de Segurança (Secure Code Review) e OWASP Top 10

---

## ⚙️ Como Executar e Testar os Projetos

### 🔹 Executando o Módulo em C (Prevenção a Overflow)
Certifique-se de possuir um compilador GCC configurado no terminal:
bash
# Compilar o arquivo gerando um executável otimizado
gcc busca_linear.c -o buffer_overflow

# Executar a aplicação e inserir dados no prompt seguro
./buffer_overflow


### 🔹 Executando o Módulo em Python (Port Scanner)
Basta ter o interpretador do Python 3 instalado em seu ambiente:
bash
python3 teste1.py
