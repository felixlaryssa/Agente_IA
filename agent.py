import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

with open("system_prompt.txt", "r", encoding="utf-8") as file:
    SYSTEM_PROMPT = file.read()

historico = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT,
    }
]

print("PyDjango Reviewer iniciado!")
print("Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Você: ").strip()

    if entrada.lower() == "sair":
        print("Encerrando agente...")
        break

    historico.append(
        {
            "role": "user",
            "content": entrada,
        }
    )

    resposta = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=historico,
    )

    conteudo = resposta.choices[0].message.content

    historico.append(
        {
            "role": "assistant",
            "content": conteudo,
        }
    )

    print(f"\nAgente: {conteudo}\n")