import streamlit as st
from PIL import Image


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
2. Nossa IA analisa os dados  
3. Você recebe uma explicação simples e dicas de economia   
""")

# Upload da imagem
uploaded_file = st.file_uploader(
    "Envie a imagem da sua conta de luz",
    type=["png", "jpg", "jpeg"]
)

# Se o usuário enviar arquivo
if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Conta enviada", use_container_width=True)

    st.success("Imagem carregada com sucesso!")

    # Botão de análise
    if st.button("Analisar conta"):
        st.info("Análise em desenvolvimento... (próxima etapa)")
