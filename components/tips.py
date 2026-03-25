def generate_tips(data):
    tips = []

    consumption = data.get("consumo_kwh", 0)
    value = data.get("valor_total", 0)
    flag = data.get("bandeira_tarifaria", "").lower()

    # 🔹 Consumo alto
    if consumption > 500:
        tips.append("🚿 Reduza o tempo de uso do chuveiro elétrico, ele é um dos maiores vilões da conta.")
        tips.append("❄️ Evite deixar geladeira aberta por muito tempo.")
        tips.append("💡 Troque lâmpadas por LED para economizar energia.")

    # 🔹 Bandeira tarifária
    if flag == "vermelha":
        tips.append("🔴 Evite usar eletrodomésticos nos horários de pico (18h às 21h).")
        tips.append("⚡ Desligue aparelhos da tomada quando não estiver usando.")
    
    elif flag == "amarela":
        tips.append("🟡 Fique atento ao consumo, pois a energia está mais cara que o normal.")

    # 🔹 Conta alta
    if value > 500:
        tips.append("📉 Tente reduzir o uso de aparelhos de alto consumo, como ferro elétrico e ar-condicionado.")

    # 🔹 Dica padrão
    tips.append("🔌 Evite deixar aparelhos em stand-by, eles continuam consumindo energia.")

    return tips