import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events

# Dados de exemplo
data = {
    'Data': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'],
    'Evento': ['Início do Projeto', 'Primeiro Marco', 'Revisão', 'Segundo Marco', 'Conclusão'],
    'Tipo': ['início', 'marco', 'revisão', 'marco', 'fim'],
    'Descrição': ['Detalhes do início...', 'Detalhes do primeiro marco...', 
                  'Detalhes da revisão...', 'Detalhes do segundo marco...', 
                  'Detalhes da conclusão...']
}

df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d').dt.date
# df['Data fim'] = pd.to_datetime(df['Data fim'], format='%Y-%m-%d').dt.date

# # Criar gráfico de linha do tempo
# fig = px.timeline(df, x_start='Data início', x_end='Data fim', 
#                   y='Evento', title='Linha do Tempo do Projeto')

# # Exibir no Streamlit
# st.plotly_chart(fig)


# Definir marcadores para cada tipo
marcadores = {
    'início': 'circle',
    'marco': 'diamond',
    'revisão': 'square',
    'fim': 'star'
}


# Definir cores para cada tipo
cores = {
    'início': 'blue',
    'marco': 'green',
    'revisão': 'orange',
    'fim': 'red'
}

# Criar figura
fig = go.Figure()

# Adicionar eventos como pontos
for tipo in df['Tipo'].unique():
    df_tipo = df[df['Tipo'] == tipo]
    fig.add_trace(go.Scatter(
        x=df_tipo['Data'],
        y=[1] * len(df_tipo),
        mode='markers+text',
        marker=dict(
            symbol=marcadores[tipo],
            size=15,
            color=cores[tipo],
            line=dict(width=2, color='DarkSlateGrey')
        ),
        text=df_tipo['Evento'],
        textposition='top center',
        name=tipo,
        customdata=df_tipo[['Evento', 'Descrição']].values,
        hoverinfo='none'
    ))

# Adicionar linha do tempo
fig.add_trace(go.Scatter(
    x=[df['Data'].min(), df['Data'].max()],
    y=[1, 1],
    mode='lines',
    line=dict(color='gray', width=2),
    showlegend=False
))

# Configurar layout
fig.update_layout(
    title='Linha do Tempo do Projeto',
    xaxis_title='Data',
    yaxis_visible=False,
    height=400,
    width=900,
    margin=dict(l=20, r=20, t=40, b=20),
    legend_title_text='Tipo de Evento'
)

# Exibir no Streamlit
st.plotly_chart(fig, use_container_width=True)

# Capturar cliques no gráfico
selected_points = plotly_events(fig, click_event=True)

selected_points

# Exibir informações do ponto clicado
if selected_points:
    point = selected_points[0]
    point_index = point['pointIndex']
    curve_number = point['curveNumber']
    
    selected_data = df.iloc[point_index]
    
    st.write(f"**Evento Selecionado:** {selected_data['Evento']}")
    st.write(f"**Descrição:** {selected_data['Descrição']}")
    st.write(f"**Data:** {selected_data['Data']}")
    st.write(f"**Tipo:** {selected_data['Tipo']}")