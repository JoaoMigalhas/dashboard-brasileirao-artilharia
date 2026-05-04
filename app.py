import streamlit as st
import pandas as pd
import plotly.express as px

#configurar pagina
st.set_page_config(
    page_title="Stats Scorers Brasileirao",
    layout= "wide"
)

st.title("Estatisticas dos Artilheiros do Brasileirao 2026!")
st.markdown("---------------")

#puxar dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/jogadores.csv")
    return df

df = carregar_dados()

#filtro de time
st.sidebar.header("Filtros")

times = ["Todos"] + sorted(df["time"].unique().tolist())

time_selecionado = st.sidebar.selectbox("Selecione o time:", times)

if time_selecionado == "Todos":
    df_filtrado = df
else:
    df_filtrado = df[df["time"] == time_selecionado]

#mostrar as stats
st.subheader("Resumo:")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de jogadores: ", len(df_filtrado))

with col2:
    st.metric("Total de gols: ", int(df_filtrado["gols"].sum()))

with col3:
     st.metric("Total de assistencias: ", int(df_filtrado["assistencias"].sum()))

st.markdown("-------------------")

#grafico teste para gols
st.subheader("Grafico de gols por jogador!")

df_gols = df_filtrado.sort_values("gols", ascending=False)

fig_gols = px.bar(
    df_gols,
    x = "jogador",
    y = "gols",
    color = "time",
    text = "gols",
    title = "Artilharia!"
)

fig_gols.update_layout(xaxis_tickangle =- 45)

st.plotly_chart(fig_gols, use_container_width = True)

st.markdown("---------------------")

#grafico teste para gols x assistencias
st.subheader("Realção Gols x Assistencias")

fig_golasist = px.scatter(
    df_filtrado,
    x = "gols",
    y = "assistencias",
    color = "time",
    size = "jogos",
    hover_name = "jogador",
    title = "Relação de gold e assistencias"
)

st.plotly_chart(fig_golasist, use_container_width=True)

st.markdown("---------------------------")

#tabela
st.subheader("Tabela completa!!")

st.dataframe(
    df_filtrado.sort_values("gols", ascending=False),
    use_container_width = True,
    hide_index = True
)