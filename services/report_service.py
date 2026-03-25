from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_report(d1, d2):
    prompt = f"""
    Você é um especialista em contas de energia elétrica no Brasil.

    Compare as duas contas abaixo e gere um relatório simples, claro e didático para um usuário comum.

    Conta anterior:
    {d1}

    Conta atual:
    {d2}

    Explique:
    - Se o consumo aumentou ou diminuiu
    - Se o valor aumentou ou diminuiu
    - Possíveis causas (bandeira, consumo, impostos)
    - Dicas simples para economizar energia

    Use linguagem simples, como se estivesse explicando para alguém leigo.
    "Separe em:
    - Resumo
    - O que mudou
    - Dicas"
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text
