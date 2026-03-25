import streamlit as st
from PIL import Image
from utils.ai_service import analyze_account
from utils.parser import extract_json, normalize_data
from components import charts
from components import explanations
from components import tips
from features.comparison import compare_accounts, gerar_insight
from components.charts import graph_comparison_of_two_accounts
from services.report_service import generate_report


st.set_page_config(
    page_title="Luz Clara",
    layout='centered'
)

# Titulo
st.title("Luz Clara")
st.subheader("Entenda sua conta de luz de forma simples")
st.markdown("""
### Como funciona?

1. Envie uma foto da sua conta de luz  
2. Nossa IA analisa os data  
3. Você recebe uma explicação simples e dicas de economia   
""")

with st.expander("Ver exemplo de foto ideal"):
    st.image("img/conta_luz.png", caption="Exemplo de foto ideal")

uploaded_file = st.file_uploader(
    "Envie a imagem da sua conta de luz",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Conta enviada", use_container_width=True)

    if st.button(" Analisar Conta"):
        with st.spinner("Analisando com IA..."):
            result = analyze_account(image)

        raw_data = extract_json(result)
        data = normalize_data(raw_data)

        if not data:
            st.error(" Não conseguimos entender sua conta. Tente outra imagem.")
        else:
            st.success("✅ Análise concluída!")

            st.subheader("📊 Resumo da Conta")

            col1, col2 = st.columns(2)

        with col1:
            st.metric("Consumo (kWh)", data["consumo_kwh"])
            st.metric("Valor Total (R$)", f'{data["valor_total"]:.2f}')

        with col2:
            st.metric("Impostos (R$)", f'{data["impostos"]:.2f}')
            st.metric("Tarifa Energia (R$)", f'{data["tarifa_energia"]:.2f}')

        st.metric(
            "Custo Energia (R$)",
            f'{(data["consumo_kwh"] * data["tarifa_energia"]):.2f}'
        )

        st.divider()

        st.subheader("📊 Para onde vai seu dinheiro?")

        fig = charts.cost_graph(data)
        st.plotly_chart(fig, use_container_width=True)

        if data["valor_total"] > 500:
            st.warning("⚠️ Sua conta está acima da média. Fique atento ao consumo!")
            
        st.divider()

        st.subheader("💡 Entenda sua conta")

        explanations = explanations.explain_account(data)

        for exp in explanations:
            st.write(exp)
        
        st.divider()

        st.subheader("💡 Dicas para economizar energia")

        tips = tips.generate_tips(data)

        for tip in tips:
            st.write(tip)

st.divider()

st.subheader("Envie duas contas para comparação")

col1, col2 = st.columns(2)

with col1:
    file1 = st.file_uploader("Conta do mês anterior", type=["png", "jpg", "jpeg"])

with col2:
    file2 = st.file_uploader("Conta do mês atual", type=["png", "jpg", "jpeg"])

if "last_file1" not in st.session_state:
    st.session_state.last_file1 = None

if "last_file2" not in st.session_state:
    st.session_state.last_file2 = None

if file1 != st.session_state.last_file1 or file2 != st.session_state.last_file2:
    st.session_state.pop("d1", None)
    st.session_state.pop("d2", None)
    st.session_state.pop("relatorio", None)

    st.session_state.last_file1 = file1
    st.session_state.last_file2 = file2

if file1 and file2:
    img1 = Image.open(file1)
    img2 = Image.open(file2)

    st.image([img1, img2], caption=["Conta anterior", "Conta atual"], width=300)

if not (file1 and file2):
    st.info("Envie as duas contas para habilitar a comparação.")

compare_button = st.button(
    "Comparar Contas",
    disabled=not (file1 and file2)
)

if compare_button:
    with st.spinner("Analisando as duas contas..."):

        r1 = analyze_account(img1)
        r2 = analyze_account(img2)

        d1 = normalize_data(extract_json(r1))
        d2 = normalize_data(extract_json(r2))

        if not d1 or not d2:
            st.error("Não foi possível analisar uma das contas.")
        else:
            st.session_state.d1 = d1
            st.session_state.d2 = d2

if "d1" in st.session_state and "d2" in st.session_state:

    d1 = st.session_state.d1
    d2 = st.session_state.d2

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📄 Conta Anterior")
        st.metric("Consumo (kWh)", d1["consumo_kwh"])
        st.metric("Valor (R$)", f'{d1["valor_total"]:.2f}')

    with col2:
        st.markdown("### 📄 Conta Atual")
        st.metric("Consumo (kWh)", d2["consumo_kwh"])
        st.metric("Valor (R$)", f'{d2["valor_total"]:.2f}')
    
    st.divider()

    fig = graph_comparison_of_two_accounts(d1, d2)
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("📊 Comparação")

    resultado = compare_accounts(d1, d2)

    st.metric(
        "Consumo",
        f"{d2['consumo_kwh']} kWh",
        delta=f"{resultado['diff_consumo']:+.0f} kWh"
    )

    st.metric(
        "Valor",
        f"R$ {d2['valor_total']:.2f}",
        delta=f"{resultado['diff_valor']:+.2f}"
    )

    st.info(gerar_insight(resultado["diff_consumo"]))

    st.divider()

    if st.button("Gerar relatório com IA"):
        with st.spinner("Gerando relatório..."):
            relatorio = generate_report(d1, d2)
        st.write(relatorio)
