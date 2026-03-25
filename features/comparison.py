def compare_accounts(d1, d2):
    diff_consumption = d2["consumo_kwh"] - d1["consumo_kwh"]
    diff_value = d2["valor_total"] - d1["valor_total"]

    return {
        "diff_consumo": diff_consumption,
        "diff_valor": diff_value
    }


def gerar_insight(diff_consumption):
    if diff_consumption > 0:
        return "📈 Seu consumo aumentou em relação ao mês anterior."
    elif diff_consumption < 0:
        return "📉 Parabéns! Você reduziu seu consumo."
    else:
        return "➡️ Seu consumo permaneceu igual."
