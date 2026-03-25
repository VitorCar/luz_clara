import json
import re


def fix_json(text):
    """
    Tenta corrigir erros comuns de JSON gerado por IA
    """
    # Adiciona vírgulas entre campos quebrados
    text = re.sub(r'"\s*"', '", "', text)
    text = re.sub(r'(\d)\s*"', r'\1, "', text)
    text = re.sub(r'"\s*(\d)', r'", \1', text)

    return text


def extract_json(texto):
    """
    Extrai o JSON de uma string (mesmo se vier com texto extra)
    """
    try:
        json_match = re.search(r'\{.*\}', texto, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            # Tenta corrigir antes de carregar
            json_str = fix_json(json_str)

            return json.loads(json_str)

    except Exception as e:
        print("Erro ao converter JSON:", e)
        return None

    return None


def normalize_data(dados):
    """
    Garante que os dados estejam no formato correto
    """

    if not dados:
        return None

    def clear_number(value):
        if isinstance(value, str):
            value = value.replace("R$", "").replace("kWh", "").strip()
            value = value.replace(",", ".")
        try:
            return float(value)
        except:
            return None

    return {
        "consumo_kwh": clear_number(dados.get("consumo_kwh")),
        "valor_total": clear_number(dados.get("valor_total")),
        "bandeira_tarifaria": dados.get("bandeira_tarifaria"),
        "impostos": clear_number(dados.get("impostos")),
        "tarifa_energia": clear_number(dados.get("tarifa_energia")),
        "iluminacao_publica": clear_number(dados.get("iluminacao_publica")),
    }
