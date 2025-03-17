import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Seus dados
data = {
    'Data': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'],
    'Evento': ['Início do Projeto', 'Primeiro Marco', 'Revisão', 'Segundo Marco', 'Conclusão'],
    'Tipo': ['início', 'marco', 'revisão', 'marco', 'fim'],
    'Descrição': ['Detalhes do início...', 'Detalhes do primeiro marco...', 'Detalhes da revisão...', 'Detalhes do segundo marco...', 'Detalhes da conclusão...']
}
df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'])

# Criar figura
fig = go.Figure()

# Adicionar eventos como pontos
fig.add_trace(go.Scatter(
    x=df['Data'],
    y=[1] * len(df),
    mode='markers+text',
    marker=dict(size=12, color='blue'),
    text=df['Evento'],
    textposition='top center',
    customdata=df['Descrição'],  # Adicionar descrições como dados personalizados
    hoverinfo='text'
))

# Configurar layout
fig.update_layout(
    title='Linha do Tempo do Projeto',
    xaxis_title='Data',
    yaxis_visible=False,
    height=300,
    width=800
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)

# Capturar cliques no gráfico
clicked_point = st.plotly_chart(fig, use_container_width=True, key='timeline')

# Exibir informações adicionais quando um ponto é clicado
if clicked_point is not None and clicked_point['points']:
    point = clicked_point['points'][0]
    st.write(f"Evento: {point['text']}")
    st.write(f"Data: {point['x']}")
    st.write(f"Descrição: {point['customdata']}")