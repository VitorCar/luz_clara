def explain_account(dados):
    explanations = []

    consumption = dados.get("consumo_kwh", 0)
    value = dados.get("valor_total", 0)
    flag = dados.get("bandeira_tarifaria", "")
    tax = dados.get("impostos", 0)
    lighting = dados.get("iluminacao_publica", 0)

    # 🔹 Consumo
    if consumption > 500:
        explanations.append(
            "⚡ Seu consumo de energia está alto. Isso pode aumentar bastante o valor da conta."
        )
    else:
        explanations.append(
            "✅ Seu consumo está dentro de um nível considerado normal."
        )

    # 🔹 Bandeira tarifária
    if flag == "vermelha":
        explanations.append(
            "🔴 A bandeira vermelha indica que a energia está mais cara devido a condições desfavoráveis de geração."
        )
    elif flag == "amarela":
        explanations.append(
            "🟡 A bandeira amarela indica um pequeno aumento no custo da energia."
        )
    elif flag == "verde":
        explanations.append(
            "🟢 A bandeira verde indica que não há custo adicional na energia."
        )

    # 🔹 Impostos
    if tax > 0:
        explanations.append(
            f"💰 Você pagou aproximadamente R$ {tax:.2f} em impostos."
        )

    if lighting > 0:
        explanations.append(
            f"💡 A taxa de iluminação pública (R$ {lighting:.2f}) é usada para manter a iluminação das ruas da sua cidade."
        )

    # 🔹 Valor total
    if value > 500:
        explanations.append(
            "⚠️ O valor total da sua conta está elevado. Vale a pena revisar seus hábitos de consumo."
        )

    return explanations