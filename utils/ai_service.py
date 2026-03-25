from google import genai
import os
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_account(imagem):
    prompt = """
    Você é um especialista em contas de energia elétrica no Brasil.

    Analise a imagem enviada e extraia as seguintes informações:

    - consumo_kwh
    - valor_total
    - bandeira_tarifaria
    - impostos
    - tarifa_energia
    - iluminacao_publica

    IMPORTANTE:
    - Responda APENAS com JSON válido
    - Use vírgulas corretamente entre todos os campos
    - NÃO escreva nenhum texto antes ou depois
    - NÃO use explicações
    - NÃO quebre o formato JSON

    Exemplo de resposta:
    {
        "consumo_kwh": number,
        "valor_total": number,
        "bandeira_tarifaria": string,
        "impostos": number,
        "tarifa_energia": number,
        "iluminacao_publica": number
    }
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            prompt,
            imagem
        ],
        config={
            "response_mime_type": "application/json"
        }
    )

    return response.text
