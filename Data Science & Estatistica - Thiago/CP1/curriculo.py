import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configuração inicial
st.set_page_config(page_title="Currículo - Gustavo Assumção", layout="wide")

# Barra lateral para navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Ir para:", ["Home", "Formação e Experiência", "Skills", "Análise de Dados"])

# Home
if pagina == "Home":
    st.title("Gustavo Bezerra Assumção")
    st.image("perfil na floresta.png", width=150)
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
    
    import os
    import pandas as pd
    import numpy as np
    import streamlit as st
    
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
    
    ### Distribuição Normal para os Retornos Diários
    st.subheader("Distribuição Normal - Retornos Diários (Último Ano)")
    from scipy.stats import norm
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(df_last_year["Return"], bins=20, density=True, alpha=0.6, color='green')
    mu, std = norm.fit(df_last_year["Return"])
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    ax.set_title(f"Distribuição Normal dos Retornos Diários (Último Ano)\n(média = {mu:.4f}, dp = {std:.4f})")
    st.pyplot(fig)
    
    st.write("""
    **Interpretação:**  
    A curva normal ajustada aos retornos diários revela que a maioria dos valores se concentra em torno da média, refletindo a volatilidade do ativo.
    """)
    
    ### Distribuição de Poisson para a contagem de dias de alta
    st.subheader("Distribuição de Poisson - Contagem de Dias de Alta (Último Ano)")
    st.write("""
    Consideramos cada dia em que o preço de fechamento supera o de abertura como um evento de "alta".  
    Agregamos esses eventos por semana para obter a contagem semanal, modelada por uma distribuição de Poisson.
    """)
    df_last_year["Up_Day"] = (df_last_year["Close"] > df_last_year["Open"]).astype(int)
    df_last_year["Week"] = pd.to_datetime(df_last_year["Date"]).dt.isocalendar().week
    weekly_up_year = df_last_year.groupby("Week")["Up_Day"].sum().reset_index()
        
    st.write("""
    **Interpretação:**  
    A modelagem com a distribuição de Poisson evidencia a frequência semanal dos dias de alta e permite avaliar se essa frequência segue o comportamento esperado para eventos discretos.
    """)
    
    ### Distribuição Binomial - Análise dos Dias de Ganho vs. Perda
    st.subheader("Distribuição Binomial - Análise dos Dias de Ganho vs. Perda")
    st.write("""
    Em mercados financeiros, cada dia de negociação pode ser considerado um experimento de Bernoulli, onde:
    - **Sucesso:** Dia com retorno positivo (ganho).
    - **Falha:** Dia com retorno negativo (perda).
    
    **Análises Propostas:**
    - **Proporção de Dias de Ganho vs. Perda:**  
      Investigar se a proporção de dias com ganho difere significativamente de 50%.
    - **Sequência de Ganhos ou Perdas:**  
      Calcular a probabilidade de ocorrer uma sequência de 5 dias consecutivos de ganhos (ou de perdas).
    - **Variação em Períodos de Alta Volatilidade:**  
      Comparar a proporção de ganhos em dias de alta e baixa volatilidade.
    """)
    
    # Cálculo da proporção de dias de ganho e perda
    df_last_year["Gain"] = (df_last_year["Return"] > 0).astype(int)
    total_days = df_last_year.shape[0]
    gain_days = df_last_year["Gain"].sum()
    loss_days = total_days - gain_days
    p_gain = gain_days / total_days
    
    st.write(f"Total de dias analisados: **{total_days}**")
    st.write(f"Dias com ganho: **{gain_days}** ({p_gain:.2%})")
    st.write(f"Dias com perda: **{loss_days}** ({(1-p_gain):.2%})")
    st.write("**Pergunta:** A proporção de dias com ganho difere significativamente de 50%?")
    
    from scipy.stats import binomtest
    result = binomtest(gain_days, total_days, p=0.5, alternative='two-sided')
    p_valor = result.pvalue
    st.write(f"P-valor do teste binomial: **{p_valor:.4f}**")

    
    # Probabilidade de observar uma sequência de 5 dias consecutivos
    seq_5_gain = p_gain ** 5
    seq_5_loss = (1 - p_gain) ** 5
    st.write(f"Probabilidade de 5 dias consecutivos de ganho: **{seq_5_gain:.4f}**")
    st.write(f"Probabilidade de 5 dias consecutivos de perda: **{seq_5_loss:.4f}**")
    
    # Análise de volatilidade
    st.write("**Análise da Proporção de Ganhos em Períodos de Alta Volatilidade:**")
    # Criar uma métrica de volatilidade relativa
    df_last_year["Volatility"] = (df_last_year["High"] - df_last_year["Low"]) / df_last_year["Open"]
    vol_threshold = df_last_year["Volatility"].median()
    df_last_year["Volatility_Level"] = np.where(df_last_year["Volatility"] >= vol_threshold, "Alta", "Baixa")
    
    gain_rate_high = df_last_year[df_last_year["Volatility_Level"]=="Alta"]["Gain"].mean()
    gain_rate_low = df_last_year[df_last_year["Volatility_Level"]=="Baixa"]["Gain"].mean()
    
    st.write(f"Período de **Alta Volatilidade** (≥ mediana): Proporção de ganhos = **{gain_rate_high:.2%}**")
    st.write(f"Período de **Baixa Volatilidade** (< mediana): Proporção de ganhos = **{gain_rate_low:.2%}**")
    st.write("""
    **Interpretação da Distribuição Binomial:**  
    - Se a proporção de ganhos estiver muito distante de 50%, isso pode indicar uma tendência ou viés no comportamento do ativo.  
    - As probabilidades de observar sequências de 5 dias consecutivos, calculadas a partir da proporção observada, ajudam a identificar padrões de momentum ou persistência.  
    - A comparação entre períodos de alta e baixa volatilidade revela se condições de mercado extremas alteram significativamente essa proporção.
    """)



# Executar o app:
# No terminal, rode: streamlit run curriculo.py
# python -m streamlit run curriculo.py