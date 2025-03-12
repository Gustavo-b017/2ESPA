import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Configuração inicial
st.set_page_config(page_title="Currículo - Gustavo Assumção", layout="wide")

# Barra lateral para navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Ir para:", ["Home", "Formação e Experiência", "Skills", "Análise de Dados"])


if pagina == "Home":
    st.title("Análise de Dados - Dados de Ações")
    
    st.header("1. Apresentação dos Dados e Tipos de Variáveis")
    st.write("""
    Este conjunto de dados contém informações históricas de uma ação, com as seguintes colunas:
    - **Date:** Data da negociação.
    - **Open, High, Low, Close:** Preços de abertura, máxima, mínima e fechamento, que são variáveis quantitativas contínuas.
    - **Volume:** Quantidade de ações negociadas (variável quantitativa discreta).
    - **Dividends:** Dividendos pagos (normalmente nulos ou discretos).
    - **Stock Splits:** Eventos de desdobramento de ações (contagem de eventos discretos).
    """)
    
    # Carregar os dados
    df = pd.read_excel("historico_btg_pactual.xlsx", parse_dates=["Date"])
    st.success("Conjunto de dados 'historico_btg_pactual.xlsx' carregado com sucesso.")
    
    st.dataframe(df.head())
    st.write("""
    **Interpretação dos Tipos de Dados:**
    - Os preços (Open, High, Low, Close) são dados quantitativos contínuos.
    - O Volume é um dado quantitativo discreto.
    """)
    
    st.subheader("Perguntas Relevantes para a Análise")
    st.write("""
    - **Qual é a distribuição dos preços de fechamento?**  
      Analisar se os preços de fechamento seguem uma distribuição normal.
      
    - **Como se comportam os retornos diários?**  
      Calcular os retornos diários (variação percentual entre Open e Close) e avaliar sua distribuição.
      
    - **Existe correlação entre o volume negociado e os retornos diários?**  
      Investigar a relação entre a quantidade negociada e a variação percentual.
      
    - **Qual a frequência de dias em que o preço fechou acima da abertura?**  
      Criar uma variável binária e analisar a contagem semanal desses eventos.
    """)
    
    # Filtrar dados do último ano para as análises
    max_date = df["Date"].max()
    df_last_year = df[df["Date"] >= (max_date - pd.DateOffset(years=1))].copy()
    df_last_year["Return"] = (df_last_year["Close"] - df_last_year["Open"]) / df_last_year["Open"]
    
    st.header("2. Medidas Centrais, Dispersão e Correlação (Último Ano)")
    
    st.write("**Estatísticas Descritivas do Conjunto de Dados:**")
    desc = df_last_year.describe()
    st.write(desc)
    st.write("""
    **Análise:**  
    As estatísticas descritivas fornecem uma visão geral sobre a tendência central, dispersão e possíveis outliers dos dados.  
    Por exemplo:
    - A média e a mediana dos preços indicam o valor central dos dados.
    - O desvio padrão demonstra a volatilidade dos preços.
    """)
      
    st.write("**Matriz de Correlação:**")
    corr = df_last_year.corr()
    st.write(corr)
    st.write("""
    **Análise da Matriz de Correlação:**  
    A matriz de correlação permite identificar relações lineares entre as variáveis.  
    Por exemplo, uma forte correlação entre 'Open' e 'Close' sugere consistência no comportamento diário da ação.
    """)
    
    st.header("3. Aplicação de Distribuições Probabilísticas (Último Ano)")
    st.write("""
    Utilizando os dados do último ano, aplicamos três abordagens:
    - **Normal:** Para modelar os **Retornos Diários**.
    - **Poisson:** Para modelar a contagem semanal de dias em que o preço fechou acima da abertura.
    - **Binomial:** Para analisar a proporção de dias de ganho vs. perda e a probabilidade de sequências de ganhos ou perdas.
    """)
    
    ###################################################################################################
    # Nova Seção: Cálculo do Lucro Diário e Classificação
    ###################################################################################################
    
    st.header("4. Análise de Lucro Diário e Previsão")
    st.write("""
    Nesta seção, calculamos o lucro diário (venda - compra) utilizando os preços de **Open** e **Close**.
    Cada dia é classificado como:
    - **Sucesso:** Lucro positivo.
    - **Fracasso:** Lucro zero ou negativo.
    """)
    
    # Cálculo do lucro diário e classificação
    df_last_year["Profit"] = df_last_year["Close"] - df_last_year["Open"]
    df_last_year["Resultado"] = np.where(df_last_year["Profit"] > 0, "Sucesso", "Fracasso")
    
    st.write("Exemplo dos dados de lucro diário e classificação:")
    st.dataframe(df_last_year[["Date", "Open", "Close", "Profit", "Resultado"]].head())
    
    # Gráfico interativo dos lucros diários com Plotly
    import plotly.express as px
    fig_profit = px.scatter(
        df_last_year, 
        x="Date", 
        y="Profit", 
        color="Resultado",
        title="Lucro Diário (Venda - Compra) e Classificação",
        labels={"Profit": "Lucro (Venda - Compra)", "Date": "Data"}
    )
    st.plotly_chart(fig_profit)
        
    # Previsão para o próximo dia usando média móvel
    st.write("### Previsão para o Próximo Dia")
    N = st.slider("Selecione o número de dias para a média móvel:", min_value=3, max_value=20, value=5, step=1)
    df_last_year = df_last_year.sort_values("Date")
    moving_avg = df_last_year["Profit"].rolling(window=N).mean()
    last_moving_avg = moving_avg.iloc[-1]
    
    st.write(f"Média móvel dos últimos {N} dias: {last_moving_avg:.2f}")
        
    if last_moving_avg > 0:
        prediction = "Sucesso"
    else:
        prediction = "Fracasso"
        
    st.write(f"Previsão para o próximo dia: **{prediction}**")
    
    st.write("""
    **Explicação do Gráfico de Lucro Diário e Classificação:**  
    Este gráfico de dispersão interativo apresenta, para cada dia, o lucro obtido (calculado como a diferença entre o preço de fechamento e o preço de abertura). Cada ponto representa um dia de negociação, sendo que:
    - A cor do ponto indica se o dia foi classificado como 'Sucesso' (lucro positivo) ou 'Fracasso' (lucro zero ou negativo).
    - A disposição dos pontos ao longo do tempo permite identificar tendências, flutuações e eventuais períodos de desempenho atípico.
    
    **Motivo e Utilidade:**  
    - **Visualização Diária:** Permite uma análise detalhada do desempenho da ação ao longo do tempo, facilitando a identificação de padrões ou anomalias.
    - **Base para Previsão:** Ao compreender a dinâmica dos lucros diários, podemos aplicar técnicas como a média móvel para prever o comportamento do próximo dia de negociação.
    - **Tomada de Decisão:** Este tipo de análise é crucial para investidores e analistas, pois evidencia de forma clara os dias de ganho e prejuízo, permitindo ajustes em estratégias de investimento.
    """)
    
    ###################################################################################################
    # Novo Gráfico: Distribuição dos Lucros Diários (Profit) via Distribuição Normal
    ###################################################################################################
    
    st.header("Distribuição dos Lucros Diários")
    st.write("""
    Este gráfico apresenta a distribuição dos lucros diários, definidos como a diferença entre o preço de fechamento e o de abertura.
    A modelagem foi realizada por meio de uma Distribuição Normal para verificar se os lucros se comportam de maneira simétrica em torno da média.
    """)
    
    # Cálculo dos parâmetros da distribuição dos lucros
    mu_profit = df_last_year["Profit"].mean()
    sigma_profit = df_last_year["Profit"].std()
    st.write(f"Estimativa de μ: {mu_profit:.2f}, σ: {sigma_profit:.2f}")
    
    fig_profit_dist = px.histogram(df_last_year, x="Profit", marginal="box", nbins=20, histnorm="probability density",
                                   title=f"Distribuição Normal dos Lucros Diários\n(média = {mu_profit:.2f}, σ = {sigma_profit:.2f})")
    st.plotly_chart(fig_profit_dist)
    
    st.write("""
    **Interpretação do Gráfico de Distribuição dos Lucros Diários:**  
    Este gráfico é fundamental para compreender como os lucros diários se distribuem ao longo do tempo. A seguir, os pontos-chave que justificam sua utilidade:
    
    - **Simetria em torno da média:** Se os lucros se distribuírem de forma simétrica, isso sugere que os dias de ganho e prejuízo tendem a se equilibrar, o que pode indicar estabilidade no desempenho do ativo.
    - **Ajuste à Distribuição Normal:** Um bom ajuste à curva normal permite utilizar métodos estatísticos para prever o comportamento futuro, baseando-se em parâmetros bem definidos (média e desvio padrão).
    - **Identificação de Outliers:** O gráfico, especialmente com o box plot marginal, facilita a identificação de outliers que podem sinalizar eventos extremos no mercado.
    - **Base para Previsão:** Entender a distribuição dos lucros é crucial para estimar a probabilidade de ocorrência de determinados resultados futuros, sendo um componente essencial na construção de modelos preditivos.
    
    Em resumo, este gráfico não só ilustra a consistência dos lucros diários, mas também fornece insights valiosos para a tomada de decisão e para o desenvolvimento de estratégias baseadas em dados históricos.
    """)
    
    st.title("Análise de Risco da Ação do BTG Pactual com Base na Distribuição Normal")
    
    st.write("""
    **Objetivo:**  
    Avaliar se vale a pena investir nas ações do BTG Pactual ao medir a relação entre retorno esperado e risco,
    utilizando medidas estatísticas derivadas da Distribuição Normal dos retornos diários.
    """)
    
    ###################################################################################################
    # 1. Cálculo dos Retornos Diários
    ###################################################################################################
    
    st.header("1. Cálculo dos Retornos Diários")
    st.write("""
    Calcularemos os log-retornos, que são mais apropriados para séries financeiras, utilizando a fórmula:
    
    \\( r_t = \\ln\\left(\\frac{P_t}{P_{t-1}}\\right) \\)
    
    onde \\( P_t \\) é o preço de fechamento no dia \\( t \\).
    """)
    
    # Carregar os dados
    df = pd.read_excel("historico_btg_pactual.xlsx", parse_dates=["Date"])
    # Calcular os log-retornos com base no preço de fechamento
    df["LogReturn"] = np.log(df["Close"] / df["Close"].shift(1))
    df = df.dropna(subset=["LogReturn"])  # Remover linhas com valores NaN
    
    st.write("Exemplo dos log-retornos calculados:")
    st.dataframe(df[["Date", "Close", "LogReturn"]].head())
    
    ###################################################################################################
    # 2. Estimativa da Distribuição Normal
    ###################################################################################################
    
    st.header("2. Estimativa da Distribuição Normal dos Retornos")
    st.write("""
    A seguir, estimamos os parâmetros da Distribuição Normal para os log-retornos:
    - **Média (\\( \\mu \\))**: Representa o retorno diário esperado.
    - **Desvio Padrão (\\( \\sigma \\))**: Mede a volatilidade diária (o risco).
    """)
    
    # Estimar os parâmetros da normal
    from scipy.stats import norm
    mu = df["LogReturn"].mean()
    sigma = df["LogReturn"].std()
    
    st.write(f"Retorno médio diário (\\( \\mu \\)): **{mu:.4f}**")
    st.write(f"Volatilidade diária (\\( \\sigma \\)): **{sigma:.4f}**")
    
    # Plotar o histograma dos log-retornos com a curva normal ajustada
    import plotly.express as px
    x_vals = np.linspace(df["LogReturn"].min(), df["LogReturn"].max(), 100)
    y_vals = norm.pdf(x_vals, mu, sigma)
    fig = px.histogram(df, x="LogReturn", nbins=50, histnorm="probability density",
                       title="Distribuição dos Log-Retornos Diários com Curva Normal Ajustada")
    fig.add_scatter(x=x_vals, y=y_vals, mode="lines", name="Curva Normal Ajustada")
    st.plotly_chart(fig)
    
    ###################################################################################################
    # 3. Cálculo do Value at Risk (VaR) e Expected Shortfall (ES)
    ###################################################################################################
    
    st.header("3. Cálculo do Value at Risk (VaR) e Expected Shortfall (ES)")
    st.write("""
    **Value at Risk (VaR):**  
    Mede a perda máxima esperada em um dia com um nível de confiança pré-determinado (ex: 95%).  
    \\( VaR = \\mu + z \\cdot \\sigma \\)  
    Onde \\( z \\) é o quantil negativo correspondente (por exemplo, \\( z \\approx -1.645 \\) para 95%).
    
    **Expected Shortfall (ES):**  
    Também conhecido como Conditional VaR, estima a perda média nos piores cenários (quando a perda excede o VaR).  
    \\( ES = \\mu - \\sigma \\cdot \\frac{\\phi(z)}{1-\\alpha} \\)  
    Onde \\( \\phi(z) \\) é a densidade da normal padrão em \\( z \\) e \\( \\alpha \\) é o nível de confiança (ex: 0.95).
    """)
    
    # Definir nível de confiança e calcular z
    alpha = 0.95
    z = norm.ppf(1 - alpha)  # Para 95% de confiança, z é aproximadamente -1.645
    
    # Calcular VaR
    VaR = mu + z * sigma
    st.write(f"**Value at Risk (VaR) a 95%:** {VaR:.4f} (ou {VaR*100:.2f}%)")
    
    # Calcular Expected Shortfall (ES)
    phi_z = norm.pdf(z)
    ES = mu - sigma * (phi_z / (1 - alpha))
    st.write(f"**Expected Shortfall (ES) a 95%:** {ES:.4f} (ou {ES*100:.2f}%)")
    
    ###################################################################################################
    # 4. Avaliação do Risco-Retorno
    ###################################################################################################
    
    st.header("4. Avaliação do Risco-Retorno")
    st.write("""
    Para avaliar a eficiência do investimento, calculamos o **Índice de Sharpe**, que relaciona o retorno esperado com o risco (volatilidade):
    
    \\( \\text{Sharpe Ratio} = \\frac{\\mu}{\\sigma} \\)
    
    Um Sharpe Ratio maior indica que o retorno compensa bem o risco assumido.
    """)
    
    Sharpe = mu / sigma
    st.write(f"**Índice de Sharpe:** {Sharpe:.4f}")
    
    ###################################################################################################
    # 5. Conclusão e Interpretação dos Resultados
    ###################################################################################################
    
    st.header("Conclusão da Análise de Risco")
    st.write("""
    Com base nos cálculos realizados:
    
    - O **VaR** indica que, com 95% de confiança, a perda máxima diária não excederá o valor calculado.
    - O **ES** estima a perda média nos piores 5% dos casos, oferecendo uma medida mais conservadora do risco.
    - O **Índice de Sharpe** fornece uma visão da relação risco-retorno.  
      
    **Decisão de Investimento:**  
    - Se o retorno médio diário (\\( \\mu \\)) for positivo e os valores de VaR e ES forem baixos, o investimento pode ser considerado promissor.  
    - Por outro lado, se a volatilidade (\\( \\sigma \\)) for elevada e os indicadores de risco (VaR e ES) indicarem perdas significativas, o risco pode superar o retorno esperado.
    """)
    
    st.write("""
    Em resumo, este código fornece as seguintes métricas essenciais:
    - **Value at Risk (VaR):** Risco máximo esperado.
    - **Expected Shortfall (ES):** Perda média em situações extremas.
    - **Índice de Sharpe:** Eficiência risco-retorno.
    
    Essas informações são fundamentais para determinar se a relação entre retorno e risco justifica o investimento na ação do BTG Pactual.
    """)

# Executar o app:
# No terminal, rode: streamlit run curriculo.py
# python -m streamlit run curriculo.py