# 💡 Luz Clara — Entenda sua Conta de Luz com IA

Aplicação web desenvolvida com **Python + Streamlit + IA (Gemini)** que permite ao usuário entender sua conta de energia elétrica de forma simples, visual e didática.

---

## 🚀 Sobre o Projeto

O **Luz Clara** nasceu com o objetivo de resolver um problema real:

> 📄 Contas de luz são complexas e difíceis de entender para a maioria das pessoas.

A aplicação permite que o usuário:

* 📸 Faça upload de uma imagem da conta de luz
* 🤖 Utilize Inteligência Artificial para extrair os dados
* 📊 Visualize gráficos claros e objetivos
* 💡 Receba explicações simples
* 📈 Compare duas contas diferentes
* 🧠 Gere um relatório inteligente com IA

---

## 🧠 Tecnologias Utilizadas

* **Python 3.11**
* **Streamlit** → Interface web
* **Google Gemini API** → IA multimodal (visão + texto)
* **Plotly** → Gráficos interativos
* **Pillow (PIL)** → Manipulação de imagens
* **Docker & Docker Compose** → Containerização
* **dotenv** → Gerenciamento de variáveis de ambiente

---

## 🏗️ Arquitetura do Projeto

```bash
luz-clara/
│
├── app.py                      # Interface principal (Streamlit)
│
├── components/                # Componentes visuais
│   ├── charts.py
│   ├── explanations.py
│   └── tips.py
│
├── services/                  # Integração com APIs
│   └── report_service.py
│
├── features/                  # Regras de negócio
│   └── comparacao.py
│
├── utils/                     # Utilitários
│   ├── ai_service.py
│   └── parser.py
│
├── img/                       # Imagens de exemplo
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

---

## ⚙️ Como Executar o Projeto

### 🔹 1. Clonar repositório

```bash
git clone https://github.com/seu-usuario/luz-clara.git
cd luz-clara
```

---

### 🔹 2. Configurar variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```env
GEMINI_API_KEY=sua_chave_aqui
```

---

### 🔹 3. Executar com Docker (RECOMENDADO)

```bash
docker-compose up --build
```

Acesse:

```text
http://localhost:8000
```

---

### 🔹 4. Executar localmente (sem Docker)

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧪 Funcionalidades

### 📸 Upload de Conta

* Envio de imagem (PNG, JPG, JPEG)
* Validação de entrada

---

### 🤖 Análise com IA

* Extração de:

  * Consumo (kWh)
  * Valor total
  * Impostos
  * Bandeira tarifária
  * Tarifa de energia

---

### 📊 Visualização

* Gráfico de distribuição de custos
* Comparação entre contas

---

### 💡 Explicação Didática

* Tradução de termos técnicos
* Linguagem acessível ao usuário

---

### 📈 Comparação entre Contas

* Diferença de consumo
* Diferença de valor
* Indicadores visuais (delta)

---

### 🤖 Relatório Inteligente

* Geração automática com IA
* Análise comparativa
* Dicas personalizadas

---

## 🧠 Conceitos Aplicados

* Integração com APIs de IA
* Processamento de dados não estruturados (imagem → JSON)
* Engenharia de prompt
* Visualização de dados
* Gerenciamento de estado no Streamlit
* Boas práticas de arquitetura (separação em camadas)
* Containerização com Docker

---

## ⚠️ Tratamento de Erros

* Validação de upload de imagens
* Tratamento de limite da API (quota)
* Mensagens amigáveis para o usuário
* Controle de estado com `st.session_state`

---

## 🔒 Segurança

* Uso de variáveis de ambiente (.env)
* Não exposição de chaves de API
* Separação de configuração e código

---

## 🚀 Próximas Melhorias

* 📄 Exportar relatório em PDF
* 👤 Sistema de login de usuários
* 📅 Histórico de contas
* 📊 Dashboard avançado
* 🤖 IA para previsão de consumo
* 🌐 Deploy em nuvem (Render / Railway)

---

## 🎯 Diferenciais do Projeto

* Uso de IA multimodal (imagem + texto)
* Foco em experiência do usuário (UX)
* Aplicação de problema real
* Estrutura profissional de código
* Containerização pronta para produção

---

## 👨‍💻 Autor

Desenvolvido por **Vitor Carvalho**

---

## 📌 Licença

Este projeto está sob a licença MIT.
