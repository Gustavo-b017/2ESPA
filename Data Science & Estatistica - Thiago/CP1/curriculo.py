import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Configuração inicial
st.set_page_config(page_title="Currículo - Gustavo Assumção", layout="wide")

# Barra lateral para navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Ir para:", ["Home", "Formação e Experiência", "Skills", "Análise de Dados"])

# Função para carregar dados financeiros
@st.cache_data
def carregar_dados(ticker):
    dados = yf.download(ticker, start="2020-01-01", end="2025-01-01")
    return dados


# Home
if pagina == "Home":
    st.title("Gustavo Bezerra Assumção")
    st.write("São Paulo, SP, Brasil")
    st.write("📧 Email: gustavobassumcaog@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/gustavo-bezerra-assumção)")

    st.header("Sobre Mim")
    st.write("""
    - 🎓 Estudante de Engenharia de Software na FIAP (2023–2027)
    - 💡 Interesse em Inteligência Artificial, Cibersegurança e Finanças
    - 🚀 Buscando estágio no BTG Pactual para aplicar conhecimento e crescer profissionalmente
    """)

# Formação e Experiência
elif pagina == "Formação e Experiência":
    st.title("Formação Acadêmica")
    st.write("🎓 FIAP - Bacharelado em Engenharia de Software (2023–2027)")

    st.title("Experiência Profissional")
    st.subheader("TC Sistemas - Desenvolvedor Full Stack (Remoto) | Jul 2024 – Out 2024")
    st.write("""
    - Desenvolvimento com PHP (Laravel) e JavaScript (Bootstrap)
    - Otimização de banco de dados MySQL
    """)

    st.subheader("Projeto Acadêmico: Sijia")
    st.write("""
    - Plataforma voltada para a experiência de pacientes pediátricos
    """)

# Skills
elif pagina == "Skills":
    st.title("Habilidades Técnicas")
    st.write("""
    - 🖥️ **Front-End:** HTML, CSS, JavaScript, React
    - ⚙️ **Back-End:** PHP, Node.js, Python
    - 🗄️ **Banco de Dados:** SQL, MySQL
    - 🔧 **Ferramentas:** Git, GitHub
    - 🎨 **Frameworks:** Laravel, Bootstrap, Tailwind
    """)

    st.title("Idiomas")
    st.write("""
    - 🇧🇷 Português – Nativo
    - 🇺🇸 Inglês – Intermediário
    - 🇨🇳 Mandarim – Iniciante
    """)

# Análise de Dados
elif pagina == "Análise de Dados":
    st.title("Análise de Dados: BTG Pactual")

    st.subheader("Introdução ao Problema")
    st.write("""
    O objetivo desta análise é estudar o desempenho histórico das ações do BTG Pactual (BPAC11) e sua relação com o mercado financeiro brasileiro.
    """)

    # Carregar dados do BTG Pactual
    dados_btg = carregar_dados("BPAC11.SA")

    # Gráfico de Preço de Fechamento
    st.subheader("Preço de Fechamento ao Longo do Tempo")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dados_btg.index, dados_btg['Close'], label='BPAC11 - Preço de Fechamento')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço de Fechamento (R$)')
    ax.legend()
    st.pyplot(fig)

    # Retornos Diários
    dados_btg['Retorno Diário'] = dados_btg['Close'].pct_change()
    st.subheader("Histograma dos Retornos Diários")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(dados_btg['Retorno Diário'].dropna(), bins=50, kde=True, ax=ax)
    ax.set_xlabel('Retorno Diário')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)

    # Média e Desvio Padrão dos Retornos
    media_retorno = dados_btg['Retorno Diário'].mean()
    desvio_retorno = dados_btg['Retorno Diário'].std()
    st.write(f"**Média dos Retornos Diários:** {media_retorno:.5f}")
    st.write(f"**Desvio Padrão dos Retornos Diários:** {desvio_retorno:.5f}")

    # Gráfico de Retornos Acumulados
    dados_btg['Retorno Acumulado'] = (1 + dados_btg['Retorno Diário']).cumprod() - 1
    st.subheader("Retorno Acumulado ao Longo do Tempo")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dados_btg.index, dados_btg['Retorno Acumulado'], label='BPAC11 - Retorno Acumulado')
    ax.set_xlabel('Data')
    ax.set_ylabel('Retorno Acumulado')
    ax.legend()
    st.pyplot(fig)

    st.write("Esta análise proporciona uma visão geral do desempenho histórico das ações do BTG Pactual, utilizando dados reais extraídos de fontes confiáveis.")

# Executar o app:
# No terminal, rode: streamlit run curriculo.py