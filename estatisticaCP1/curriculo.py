"""
Aplicativo Currículo - Gustavo Bezerra Assumção
Autor: Gustavo Bezerra Assumção
Descrição: Exibe informações pessoais, acadêmicas, profissionais e análises de dados.
"""

# Imports necessários
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
from scipy.stats import norm

# Configuração da página
st.set_page_config(
  page_title="Currículo - Gustavo Assumção",
  layout="wide"
)

# Barra lateral para navegação
with st.sidebar:
  st.title("Navegação")
  pagina = st.radio("Ir para:", ["Home", "Formação e Experiência", "Skills", "Análise de Dados"])

# Conteúdo da página "Home"
if pagina == "Home":
  st.title("Gustavo Bezerra Assumção")
  st.image("perfil na floresta.png", width=200)
  st.write("São Paulo, SP, Brasil")
  st.write("📧 Email: gustavobassumcaog@gmail.com")
  st.write("🔗 [LinkedIn](https://www.linkedin.com/in/gustavo-bezerra-assum%C3%A7%C3%A3o-829202289/)")
  st.header("Sobre Mim")
  st.write("""
    EU sou estudante de Engenharia de Software na FIAP desde 2023. Nascido em Palmas - TO, atualmente resido em São Paulo - SP.

    Características Pessoais:

    * Sou trabalhador, autodidata e de mente aberta, sempre buscando novas oportunidades de 
    aprendizado.

    * Criativo e ambicioso, sou apaixonado por tecnologia e inovação, o que me impulsiona a explorar 
    soluções modernas e eficientes.

    Interesses e Desenvolvimento Pessoal:

    * Tenho um forte interesse em estudar comportamento humano para melhorar minhas habilidades 
    interpessoais e me tornar a melhor versão de mim mesmo.

    * Busco constantemente o crescimento pessoal e profissional, visando entender melhor os outros e 
    contribuir positivamente em qualquer ambiente.


    Competências Técnicas:

    * Experiência prática em desenvolvimento full stack, com habilidades em:
        * HTML e CSS
        * JavaScript
        * React
        * PHP com Laravel
        * Bancos de dados como MySQL e SQL Server
        * Java
        * Git e GitHub

    * Comprometido com o aprendizado contínuo, possuo certificações em:
        * SQL
        *Java
        * Python
        * BlockChain 
        * Git e GitHub

    Objetivos Profissionais:

    * Estou em busca de oportunidades, onde possa aplicar minhas habilidades para integrar tecnologia e 
    estratégia de negócios.

    * Desejo contribuir para projetos inovadores que gerem valor real, utilizando minha capacidade de 
    colaboração e sinergia em equipe para alcançar resultados excepcionais.

    Acredito que minha combinação de habilidades técnicas, paixão por inovação e capacidade de trabalhar bem em equipe me torna uma adição valiosa para qualquer organização. Estou sempre pronto para enfrentar desafios e criar soluções impactantes.
  """)

# Formação e Experiência
elif pagina == "Formação e Experiência":
  st.title("Formação Acadêmica")
  st.write("🎓 FIAP - Bacharelado em Engenharia de Software (2023–2027)")

  st.title("Experiência Profissional")
  st.subheader("TC Sistemas - Desenvolvedor Full Stack (Remoto) | Jul 2024 – Out 2024")
  st.write("""
    Desenvolvi o front-end e o back-end.
    * Usando php (laravel 11). 
    * Fiz as funcionalidades e efeitos com o javascript e com o bootstrap.
    * Montando o layout em HTML, com estilização do CSS puro (tudo dentro do laravel 11). 
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
    - ⚙️ **Back-End:** PHP, Node.js, Python, Java, .NET
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

elif pagina == "Análise de Dados":
  st.title("Análise de Dados - Ação do BTG Pactual")
  
  ###########################################
  # 1. Apresentação dos Dados e Tipos de Variáveis
  ###########################################
  st.header("1. Apresentação dos Dados e Tipos de Variáveis")
  st.write("""
    Este conjunto de dados contém informações históricas de uma ação, com as seguintes colunas:
    - **Date:** Data da negociação.
    - **Open, High, Low, Close:** Preços de abertura, máxima, mínima e fechamento (variáveis quantitativas contínuas).
    - **Volume:** Quantidade de ações negociadas (variável quantitativa discreta).
  """)
  
  # Carregar os dados
  df = pd.read_excel("data/historico_btg_pactual.xlsx", parse_dates=["Date"])
  st.success("Conjunto de dados '/historico_btg_pactual.xlsx' carregado com sucesso.")
  st.dataframe(df.head())
  
  st.write("""
    **Interpretação dos Tipos de Dados:**
    - Preços (Open, High, Low, Close): Dados quantitativos contínuos.
    - Volume: Dado quantitativo discreto.
  """)
  
  # Filtrar dados do último ano para análises
  max_date = df["Date"].max()
  df_last_year = df[df["Date"] >= (max_date - pd.DateOffset(years=1))].copy()
  df_last_year["Return"] = (df_last_year["Close"] - df_last_year["Open"]) / df_last_year["Open"]
  
  ###########################################
  # 2. Estatísticas Descritivas e Correlações (Último Ano)
  ###########################################

  st.header("2. Medidas Centrais, Dispersão e Correlação (Último Ano)")

  # Exibição das Estatísticas Descritivas
  st.write("**Estatísticas Descritivas do Conjunto de Dados:**")
  desc = df_last_year.describe()
  st.write(desc)

  # Insights Exclusivamente Extraídos da Tabela de Estatísticas Descritivas
  st.write("""
    **Insights Extraídos da Tabela de Estatísticas Descritivas:**

    1. **Valor Central dos Dados:**  
      A média e a mediana indicam que os preços se concentram em torno de um valor central consistente, sugerindo estabilidade na formação dos preços.

    2. **Volatilidade Observada:**  
      O desvio padrão revela o grau de dispersão dos preços, apontando para variações significativas que podem impactar a negociação diária do ativo.

    3. **Amplitude dos Valores:**  
      Os valores mínimo e máximo destacam a amplitude dos dados, evidenciando a ocorrência de eventos extremos que merecem atenção para uma análise de risco detalhada.
  """)

  # Gráfico Boxplot para Visualização da Distribuição dos Preços
  fig_box = px.box(
    df_last_year, 
    y=["Open", "Close", "High", "Low"],
    title="Distribuição dos Preços Diários (Boxplot)",
    labels={"value": "Preço", "variable": "Tipo de Preço"}
  )
  st.plotly_chart(fig_box)

  # Insights Exclusivos do Gráfico Boxplot
  st.write("""
    **Insights Extraídos do Boxplot:**

    1. **Concentração dos Dados:**  
      O boxplot mostra claramente a mediana e os quartis, evidenciando onde os preços se concentram e indicando a consistência dos valores diários.

    2. **Identificação de Outliers:**  
      Os pontos que se encontram fora dos "bigodes" representam outliers, sugerindo dias com variações de preço incomuns que podem estar relacionados a eventos específicos do mercado.

    3. **Intervalo Interquartil (IQR):**  
      A distância entre o primeiro e o terceiro quartil fornece uma medida robusta da dispersão dos preços, destacando a variabilidade típica dos valores sem a influência dos extremos.

    4. **Comparação Entre Tipos de Preço:**  
      A sobreposição dos boxplots para 'Open', 'Close', 'High' e 'Low' permite comparar visualmente a distribuição de cada variável, facilitando a identificação de similaridades e diferenças no comportamento diário do ativo.

    5. **Sinal de Assimetria:**  
      Se algum boxplot apresentar assimetria (com a mediana deslocada em relação ao centro da caixa), isso pode indicar uma tendência de concentração de preços em uma das extremidades, sugerindo possíveis distorções no comportamento do mercado.
  """)

  # Exibição da Matriz de Correlação
  st.write("**Matriz de Correlação:**")
  corr = df_last_year.corr()
  st.write(corr)

  # Gráfico Heatmap da Matriz de Correlação
  fig_corr = px.imshow(corr, text_auto=True, title="Heatmap da Matriz de Correlação")
  st.plotly_chart(fig_corr)

  # Insights Exclusivamente Extraídos da Matriz de Correlação
  st.write("""
    **Insights Extraídos da Matriz de Correlação:**

    1. **Relação Entre Preços de Abertura e Fechamento:**  
      Uma forte correlação entre 'Open' e 'Close' indica que os preços de abertura e fechamento se movem de forma consistente, refletindo um comportamento diário coeso do ativo.

    2. **Interdependência dos Indicadores de Preço:**  
      As variáveis 'High' e 'Low' também apresentam correlações significativas com 'Open' e 'Close', sugerindo que os movimentos de preço durante o pregão estão inter-relacionados.

    3. **Implicações para Análise de Risco:**  
      As correlações elevadas entre as variáveis destacam que alterações em uma dimensão dos preços podem afetar as demais, sendo um ponto crucial para modelar riscos e prever oscilações do ativo.
  """)

  ###########################################
  # 3. Análise de Lucro Diário e Previsão
  ###########################################

  st.header("3. Análise de Lucro Diário e Previsão")

  st.write("""
    Nesta seção, calculamos o lucro diário (diferença entre os preços de **Close** e **Open**) e classificamos cada dia como:
    - **Sucesso:** quando o lucro é positivo;
    - **Fracasso:** quando o lucro é zero ou negativo.
  """)

  # Cálculo do lucro diário e classificação
  df_last_year["Profit"] = df_last_year["Close"] - df_last_year["Open"]
  df_last_year["Resultado"] = np.where(df_last_year["Profit"] > 0, "Sucesso", "Fracasso")

  st.write("Exemplo dos dados de lucro diário e sua classificação:")
  st.dataframe(df_last_year[["Date", "Open", "Close", "Profit", "Resultado"]].head())

  # Gráfico interativo dos lucros diários com Plotly
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

  # Insights Exclusivamente Extraídos do Gráfico
  st.write("""
    **Insights Extraídos do Gráfico de Lucro Diário e suas Respostas:**

    1. **Qual é o padrão de distribuição dos lucros diários?**  
    O gráfico revela uma dispersão equilibrada em torno do zero, mostrando que a maioria dos dias apresenta lucros moderados, com uma distribuição relativamente simétrica entre ganhos e perdas.

    2. **Como os pontos de dados se agrupam ao longo do tempo?**  
    Observa-se que os dados se agrupam em períodos onde predominam dias classificados como 'Sucesso' ou 'Fracasso', evidenciando fases consistentes de desempenho positivo ou negativo do ativo.

    3. **Quais são os sinais de volatilidade no comportamento diário do ativo?**  
    A variabilidade dos pontos em torno da linha zero indica que, mesmo havendo muitos dias com retornos moderados, ocorrem dias com variações acentuadas, refletindo períodos de alta volatilidade.

    4. **Como a classificação 'Sucesso' e 'Fracasso' se distribui temporalmente?**  
    A diferenciação por cores no gráfico permite identificar períodos em que os dias lucrativos ou não lucrativos se alternam, sugerindo tendências temporais que podem estar ligadas a eventos de mercado específicos.

    5. **O que a média móvel dos últimos N dias indica sobre o comportamento recente?**  
    A média móvel oferece uma visão do desempenho recente: quando o valor é positivo, há uma tendência de dias lucrativos; quando é negativo, sugere uma predominância de prejuízos, ajudando a fundamentar a previsão para o próximo dia.
  """)
  
  ###########################################
  # 4. Distribuição dos Lucros Diários
  ###########################################

  st.header("4. Distribuição dos Lucros Diários")
  st.write("""
    Este gráfico apresenta a distribuição dos lucros diários, definidos como a diferença entre o preço de fechamento e o de abertura.  
    Utilizamos uma modelagem por Distribuição Normal para avaliar se os lucros se distribuem de forma simétrica em torno da média, permitindo inferências diretas sobre o comportamento dos retornos diários.
  """)

  # Cálculo dos parâmetros da distribuição
  mu_profit = df_last_year["Profit"].mean()
  sigma_profit = df_last_year["Profit"].std()
  st.write(f"Estimativa de μ (média): {mu_profit:.2f}, σ (desvio padrão): {sigma_profit:.2f}")

  # Criação do histograma com box plot marginal para identificação de outliers
  fig_profit_dist = px.histogram(
    df_last_year, 
    x="Profit", 
    marginal="box", 
    nbins=20, 
    histnorm="probability density",
    title=f"Distribuição Normal dos Lucros Diários\n(média = {mu_profit:.2f}, σ = {sigma_profit:.2f})"
  )

  # Exibir o gráfico interativo
  st.plotly_chart(fig_profit_dist)

  st.write("""
    **Interpretação e Insights do Gráfico:**

    - **Distribuição Simétrica:**  
      O gráfico demonstra que os lucros diários se distribuem de forma aproximadamente simétrica em torno da média, indicando um equilíbrio entre dias de ganhos e prejuízos.

    - **Parâmetros Estatísticos Relevantes:**  
      Os valores de μ e σ oferecem uma visão clara do retorno médio diário e da volatilidade. Pela regra dos 68-95-99.7, cerca de 68% dos dias apresentam lucros dentro do intervalo μ ± σ, reforçando a estabilidade estatística do ativo.

    - **Identificação de Outliers:**  
      O box plot marginal evidencia a presença de pontos que se desviam significativamente da tendência central, indicando dias com eventos extraordinários ou choques de mercado que podem influenciar fortemente o comportamento das ações.

    - **Relação entre Risco e Retorno:**  
      A dispersão dos dados, medida pelo desvio padrão, permite inferir a relação entre risco e retorno. Uma dispersão ampla sugere maior volatilidade, enquanto uma concentração dos dados em torno da média indica um comportamento mais previsível e menor risco associado.

    - **Frequência dos Retornos:**  
      A concentração da maior parte dos retornos próximos à média demonstra que, na maioria dos dias, os lucros ou perdas são moderados. Essa característica reforça que, apesar de ocorrerem variações significativas em alguns dias, esses eventos extremos são menos frequentes.

    - **Comportamento da Cauda da Distribuição:**  
      As caudas do histograma indicam a ocorrência de eventos raros com retornos muito altos ou muito baixos, oferecendo uma visão sobre a probabilidade de eventos extremos, que são cruciais para a avaliação de risco do ativo.

    - **Prevalência dos Retornos Moderados:**  
      O pico da distribuição, que se concentra em torno de valores próximos à média, evidencia que o comportamento diário do ativo tende a ser moderado, sugerindo previsibilidade e consistência nas oscilações de preços.
  """)
  
  ###########################################
  # 5. Análise Dinâmica com Janelas Móveis
  ###########################################
  st.header("5. Análise Dinâmica com Janelas Móveis")

  # Definir o slider para o tamanho da janela antes de utilizá-lo no texto
  window_size = st.slider("Selecione o tamanho da janela (dias):", min_value=5, max_value=60, value=30, step=5)

  st.write(f"""
    Nesta seção, exploramos a evolução dos lucros diários através de janelas móveis, considerando os últimos **{window_size}** dias.  
    Ao calcular a **média móvel** e o **desvio padrão móvel** dos lucros, obtemos insights dinâmicos que permitem:
    - **Identificar a tendência central:** A média móvel suaviza as oscilações diárias, revelando a direção geral dos lucros – seja uma tendência de crescimento, estabilidade ou declínio.
    - **Mensurar a volatilidade do mercado:** O desvio padrão móvel indica os períodos de maior ou menor instabilidade, possibilitando a identificação de eventos ou mudanças significativas.
    - **Auxiliar na tomada de decisão:** A análise conjunta dessas métricas oferece subsídios para estratégias de investimento, mostrando quando o risco pode estar aumentando ou quando os lucros se tornam mais consistentes.
  """)

  # Garantir que os dados do último ano estejam ordenados por Data
  df_last_year = df_last_year.sort_values("Date")

  # Cálculo da média móvel e do desvio padrão móvel para a coluna 'Profit'
  df_last_year["Rolling_Mean"] = df_last_year["Profit"].rolling(window=window_size).mean()
  df_last_year["Rolling_Std"] = df_last_year["Profit"].rolling(window=window_size).std()

  st.write(f"Mostrando os cálculos com uma janela de **{window_size}** dias.")

  # Criar um gráfico interativo com Plotly para exibir a evolução da média móvel e do desvio padrão móvel
  import plotly.graph_objects as go

  fig_moving = go.Figure()
  fig_moving.add_trace(go.Scatter(
    x=df_last_year["Date"], 
    y=df_last_year["Rolling_Mean"], 
    mode='lines',
    name=f'Média Móvel ({window_size} dias)',
    line=dict(color='blue')
  ))
  fig_moving.add_trace(go.Scatter(
    x=df_last_year["Date"], 
    y=df_last_year["Rolling_Std"], 
    mode='lines',
    name=f'Desvio Padrão Móvel ({window_size} dias)',
    line=dict(color='red')
  ))
  fig_moving.update_layout(
    title="Evolução Dinâmica dos Lucros Diários",
    xaxis_title="Data",
    yaxis_title="Valor",
    template="plotly_white"
  )
  st.plotly_chart(fig_moving)

  st.write("""
    **Interpretação e Insights Adicionais:**
    - **Tendência de Longo Prazo:**  
      A média móvel suaviza as variações diárias, permitindo identificar se os lucros estão, em geral, em ascensão, estagnação ou declínio. Uma tendência ascendente pode sugerir robustez no desempenho, enquanto uma descida pode sinalizar desafios.
    - **Identificação de Períodos de Instabilidade:**  
      Picos no desvio padrão móvel evidenciam momentos de alta volatilidade. Esses períodos podem estar associados a eventos de mercado ou notícias que impactam significativamente os lucros.
    - **Relação entre Média e Volatilidade:**  
      Ao comparar a evolução da média móvel com a do desvio padrão, é possível perceber se o aumento do risco (volatilidade) acompanha uma melhora ou deterioração nos lucros. Por exemplo, um aumento no desvio padrão sem crescimento na média pode indicar maior risco sem retorno compensatório.
    - **Aplicabilidade para Decisões Estratégicas:**  
      Esses insights dinâmicos são fundamentais para a tomada de decisão. Identificar períodos de baixa volatilidade e tendências de crescimento pode orientar momentos oportunos para investir ou ajustar estratégias, enquanto aumentos bruscos na volatilidade podem sinalizar a necessidade de ações de mitigação de risco.
    - **Comparação Temporal:**  
      Ao variar o tamanho da janela, o usuário pode comparar diferentes períodos, permitindo uma análise mais granular e a detecção de mudanças de regime no comportamento dos lucros.
  """)

  ###########################################
  # 6. Análise da Distribuição Normal na Janela Atual
  ###########################################
  st.header("6. Análise da Distribuição Normal na Janela Atual")
  st.write(f"""
    Nesta seção, focamos na análise dos lucros diários observados na janela móvel atual, que corresponde aos últimos **{window_size}** dias. Através da aplicação da Distribuição Normal, buscamos:
    - **Verificar a simetria dos dados:** Confirmar se os lucros diários se distribuem de forma equilibrada, sem inclinação pronunciada para ganhos ou perdas.
    - **Estimar os parâmetros estatísticos fundamentais:** Determinar a média (μ), que representa o desempenho médio dos lucros, e o desvio padrão (σ), que reflete a volatilidade do mercado nesse período.
    - **Avaliar o risco inerente:** Um desvio padrão elevado indica maior incerteza e risco de variações extremas nos lucros, permitindo quantificar a probabilidade de ocorrência de perdas significativas.
    - **Apoiar a escolha de modelos preditivos:** Caso os dados se ajustem à Distribuição Normal, métodos estatísticos e preditivos que partem dessa premissa podem ser empregados com mais confiança.
    - **Fornecer insights estratégicos adicionais:** A análise dos parâmetros e da forma da distribuição ajuda a definir limites de perdas (VaR), identificar tendências e comparar o comportamento atual com períodos anteriores.
  """)

  # Selecionar dados da janela móvel atual (últimos window_size dias)
  window_data = df_last_year.tail(window_size)

  # Cálculo dos parâmetros da Distribuição Normal para a janela atual
  mu_window = window_data["Profit"].mean()
  sigma_window = window_data["Profit"].std()

  st.write(f"Parâmetros estimados para a janela atual: **μ = {mu_window:.2f}** e **σ = {sigma_window:.2f}**.")

  # Teste de normalidade (Shapiro-Wilk) para verificar se os dados se ajustam à normal
  from scipy.stats import shapiro
  stat, p_value = shapiro(window_data["Profit"])
  st.write("**Teste Shapiro-Wilk:**")
  st.write(f"Estatística: {stat:.4f}, p-valor: {p_value:.4f}")
  if p_value > 0.05:
    st.write("Os dados na janela atual podem ser considerados como provenientes de uma Distribuição Normal.")
  else:
    st.write("Os dados na janela atual **não** seguem uma distribuição normal idealmente.")

  # Plotar o histograma dos lucros da janela atual com a curva da Distribuição Normal ajustada
  import plotly.graph_objects as go
  x_min = window_data["Profit"].min()
  x_max = window_data["Profit"].max()
  x_range = np.linspace(x_min, x_max, 100)
  y_norm = norm.pdf(x_range, mu_window, sigma_window)

  fig_norm = go.Figure()
  fig_norm.add_trace(go.Histogram(
    x=window_data["Profit"],
    nbinsx=10,
    histnorm="probability density",
    name="Histograma",
    marker_color='lightblue',
    opacity=0.75
  ))
  fig_norm.add_trace(go.Scatter(
      x=x_range,
      y=y_norm,
      mode='lines',
      name="Distribuição Normal Ajustada",
      line=dict(color='red', width=2)
  ))
  fig_norm.update_layout(
      title="Histograma dos Lucros Diários na Janela Atual com Curva Normal",
      xaxis_title="Lucro Diário",
      yaxis_title="Densidade de Probabilidade",
      template="plotly_white"
  )
  st.plotly_chart(fig_norm)

  # Cálculos adicionais para extrair mais insights do gráfico
  # Probabilidade de um lucro negativo
  prob_neg = norm.cdf(0, mu_window, sigma_window)
  # Valor em Risco (VaR) a 5%: em 5% dos casos, o lucro diário será inferior a esse valor
  VaR_5 = norm.ppf(0.05, mu_window, sigma_window)

  st.write(f"**Probabilidade de Lucro Negativo:** {prob_neg*100:.2f}%")
  st.write(f"**Valor em Risco (VaR) a 5%:** {VaR_5:.2f}")

  st.write(f"""
    **Insights Adicionais Extraídos da Análise:**
    - **Confiabilidade dos Parâmetros:** A estimativa de **μ = {mu_window:.2f}** e **σ = {sigma_window:.2f}** fornece uma visão clara do desempenho médio e da volatilidade recente dos lucros. Parâmetros estáveis indicam um comportamento previsível.
    - **Probabilidade de Resultados Adversos:** Com aproximadamente **{prob_neg*100:.2f}%** de chance de ocorrer um lucro negativo, é possível mensurar o risco diário e ajustar estratégias de proteção ou hedge.
    - **Valor em Risco (VaR):** O VaR a 5% de **{VaR_5:.2f}** serve como um parâmetro crítico para definir limites operacionais e planos de contingência, ajudando a mitigar perdas em cenários extremos.
    - **Dinamismo do Mercado:** A análise na janela atual permite comparar esses parâmetros com períodos anteriores. Mudanças significativas podem sinalizar alterações no comportamento do mercado, como aumento de volatilidade ou mudança na tendência central.
    - **Aplicabilidade Preditiva e Simulações:** Um bom ajuste à Distribuição Normal permite o uso de simulações de Monte Carlo e outras técnicas preditivas, contribuindo para a elaboração de cenários futuros e estratégias de investimento.
    - **Comparação com Modelos Alternativos:** Caso os dados não se ajustem perfeitamente à normal, esses insights podem motivar a investigação de distribuições alternativas, proporcionando uma análise mais robusta e informada.
  """)
    




# Para rodar o app, utilize:
# streamlit run curriculo.py
# ou
# python -m streamlit run curriculo.py
