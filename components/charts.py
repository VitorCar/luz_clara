import plotly.express as px
import plotly.graph_objects as go


def cost_graph(data):
    labels = []
    valores = []

    consumption = data.get("consumo_kwh", 0)
    fare = data.get("tarifa_energia", 0)

    custo_energia = consumption * fare

    if custo_energia:
        labels.append("Energia")
        valores.append(custo_energia)

    if data.get("impostos"):
        labels.append("Impostos")
        valores.append(data["impostos"])

    if data.get("iluminacao_publica"):
        labels.append("Iluminação Pública")
        valores.append(data["iluminacao_publica"])

    fig = px.pie(
        names=labels,
        values=valores,
        title="Distribuição dos Custos da Conta"
    )

    return fig

def graph_comparison_of_two_accounts(d1, d2):

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Conta Anterior',
        x=['Consumo', 'Valor'],
        y=[d1['consumo_kwh'], d1['valor_total']]
    ))

    fig.add_trace(go.Bar(
        name='Conta Atual',
        x=['Consumo', 'Valor'],
        y=[d2['consumo_kwh'], d2['valor_total']]
    ))

    fig.update_layout(barmode='group', title="Comparação entre contas")

    return fig
