# Agente_IA

# Revisor PyDjango

Agente conversacional simples especializado em revisão de código Python e Django, desenvolvido como atividade do Grupo de Estudos de Inteligência Artificial com foco em Engenharia de Prompt e construção de agentes conversacionais.

O agente utiliza um modelo LLM via API da OpenRouter e é capaz de:

- Manter contexto entre múltiplos turnos da conversa;
- Revisar trechos de código Python/Django;
- Explicar erros e sugerir melhorias;
- Recusar perguntas fora do escopo definido no system prompt.

---

## Tecnologias Utilizadas

- Python
- OpenRouter API
- OpenAI SDK
- python-dotenv

---

## Como Rodar o Projeto

### 1. Instale as dependências

```bash
pip3 install openai python-dotenv
```

### 2. Execute o agente

```bash
python3 agent.py
```

## Estrutura do Projeto

```bash
Agente_IA/
├── .env                 # Chave da API da OpenRouter
├── .gitignore           # Arquivos ignorados pelo Git
├── agent.py             # Código principal do agente conversacional
├── README.md            # Documentação do projeto
├── reflexao.pdf         # Reflexão escrita da atividade
└── system_prompt.txt    # Prompt que define o comportamento do agente