import streamlit as st
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv("vendas.csv")

st.write("#Sistema de Vendas")
Data = st.sidebar.date_input("Data da Venda")
Vendedor = st.sidebar.selectbox("vendedor", ["Thiago", "Everson", "Nicolas"])
Produto = st.sidebar.selectbox("produto", ["Notebook", "Celular", "Fone"])
Quantidade = st.sidebar.number_input("Quantidade", step=1)
Valor = st.sidebar.number_input("Valor")
Botao = st.sidebar.button("Cadastrar Venda")

if Botao:
    nova_venda = [Data, Vendedor, Produto, Quantidade, Valor]
    tabela_vendas.loc[len(tabela_vendas)] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada com sucesso!")

st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

st.write("## Dashboard")
faturamento = tabela_vendas["Valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

grafico1 = px.bar(tabela_vendas, x="Vendedor", y="Valor", color="Produto")
st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_vendas, names="Produto", values="Valor")
st.plotly_chart(grafico2)

st.sidebar.write("## Cadastrar Venda")
