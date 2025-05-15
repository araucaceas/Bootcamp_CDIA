
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard de Resultados", layout="wide")
st.title("Dashboard - Classificação de Falhas em Chapas de Aço Inoxidável")

aba = st.sidebar.radio("Navegação", ["Visão Geral", "Métricas por Classe", "Conclusão"])

df_metrics = pd.read_csv("metricas_por_classe.csv")

if aba == "Visão Geral":
    st.subheader("Objetivo do Projeto")
    st.markdown("""
    Desenvolver um modelo de aprendizado de máquina multi‑rótulo para detectar até **7 categorias de falhas**
    em chapas de aço inoxidável, utilizando variáveis como espessura, temperatura e peso da placa.
    """)
    st.subheader("Resumo de Desempenho Global")
    st.metric("Acurácia Macro Média", "91,96%")
    st.metric("ROC AUC Média", "92,56%")

elif aba == "Métricas por Classe":
    st.subheader("Desempenho por Classe de Falha")
    st.dataframe(df_metrics.style.format("{:.2%}", subset=["Acurácia", "Precisão", "Recall", "F1-Score", "ROC AUC"]))

    st.markdown("### F1-Score por Classe")
    fig, ax = plt.subplots()
    sns.barplot(data=df_metrics, x="Classe", y="F1-Score", palette="Blues_d", ax=ax)
    ax.set_ylabel("F1-Score")
    ax.set_ylim(0, 1)
    st.pyplot(fig)

elif aba == "Conclusão":
    st.subheader("Resumo Final e Recomendações")
    st.success("O modelo teve ótimo desempenho geral, especialmente para falha_3 e falha_4.")
    st.markdown("""
    - **Pontos fortes:** alta acurácia geral, bom equilíbrio de F1 nas principais falhas.
    - **Desafios:** baixa sensibilidade (recall) para falha_1 e falha_5.
    - **Próximos passos:** balanceamento das classes minoritárias, ajuste de thresholds e uso de modelos como XGBoost.
    """)
