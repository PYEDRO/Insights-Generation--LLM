import streamlit as st
import pandas as pd
import torch
from transformers import pipeline
import matplotlib.pyplot as plt

# Configura o dispositivo: usa GPU se disponível, caso contrário, CPU
device = 0 if torch.cuda.is_available() else -1

# Inicializa o pipeline de geração de texto com o modelo DistilGPT2
generator = pipeline("text-generation", model="distilgpt2", device=device)

# Título e descrição da aplicação
st.title("Análise de Dataset com Geração de Insights via LLM")
st.write("Carregue seu dataset em formato CSV e deixe o LLM analisar e sugerir insights com base nos dados.")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Selecione um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Leitura do dataset
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Visualização do Dataset")
    st.write(df.head())
    
    st.subheader("Estatísticas Descritivas")
    st.write(df.describe())
    
    st.subheader("Tipos de Dados")
    st.write(df.dtypes)
    
    # Cria um resumo textual do dataset para enviar ao LLM
    resumo = "Resumo do Dataset:\n\n"
    resumo += "Estatísticas Descritivas:\n" + df.describe().to_string() + "\n\n"
    resumo += "Tipos de Dados:\n" + df.dtypes.to_string() + "\n"
    
    st.subheader("Resumo Gerado para Análise")
    st.text_area("Resumo do Dataset", value=resumo, height=300)
    
    # Botão para gerar insights a partir do resumo
    if st.button("Gerar Insights"):
        with st.spinner("Analisando dataset e gerando insights..."):
            prompt = (
                "A seguir, um resumo de um dataset foi apresentado. Com base nessas informações, "
                "identifique os principais padrões, tendências e possíveis problemas, e sugira caminhos para aprofundar a análise.\n\n"
                f"{resumo}\n\n"
                "Insights:"
            )
            # Gera os insights com limite de 200 tokens
            insights = generator(prompt, max_length=200, num_return_sequences=1)
            insights_text = insights[0]['generated_text']
        
        st.subheader("Insights Gerados pelo LLM")
        st.write(insights_text)
        
    # Exemplo opcional: exibir um gráfico simples caso haja dados numéricos
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if numeric_cols:
        st.subheader("Visualização de Dados Numéricos")
        coluna = st.selectbox("Selecione uma coluna numérica para visualizar", numeric_cols)
        fig, ax = plt.subplots()
        ax.hist(df[coluna].dropna(), bins=20, color="skyblue", edgecolor="black")
        ax.set_title(f"Distribuição de {coluna}")
        ax.set_xlabel(coluna)
        ax.set_ylabel("Frequência")
        st.pyplot(fig)
