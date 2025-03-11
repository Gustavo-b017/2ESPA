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
        - **Date:** Data da negociação. Variável temporal que indica o dia específico da transação.
        - **Open, High, Low, Close:** Preços de abertura, máxima, mínima e fechamento. Variáveis quantitativas contínuas, que são fundamentais para entender o comportamento da ação durante o dia.
        - **Volume:** Quantidade de ações negociadas. Variável quantitativa discreta que indica o nível de liquidez do ativo.
        - **Dividends:** Dividendos pagos. Variável discreta, que geralmente tem valores nulos, mas pode ser importante para análise de rentabilidade.
        - **Stock Splits:** Eventos de desdobramento de ações. Contagem de eventos discretos que podem afetar o valor nominal das ações.
    """)        

    
    import pandas as pd
    import numpy as np
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
    
    # Filtrar dados do último ano para as análises estatísticas e probabilísticas
    max_date = df["Date"].max()
    df_last_year = df[df["Date"] >= (max_date - pd.DateOffset(years=1))].copy()
    df_last_year["Return"] = (df_last_year["Close"] - df_last_year["Open"]) / df_last_year["Open"]
    
    st.header("2. Medidas Centrais, Dispersão e Correlação (Último Ano)")
    
    st.write("**Estatísticas Descritivas do Conjunto de Dados:**")
    desc = df_last_year.describe()
    st.write(desc)
    st.write("""
    **Análise:**  
    Esta tabela resume as principais medidas de tendência central e dispersão para as variáveis numéricas do último ano.  
    Ela permite responder perguntas como:
    - Qual é a média e mediana dos preços e volumes?
    - Qual o nível de variabilidade (desvio padrão) nos preços?
    - Há presença de valores extremos que possam afetar a análise?
    Esses insights são fundamentais para compreender a distribuição dos dados e identificar possíveis necessidades de transformação ou análise adicional.
    """)
    
    
       
    st.write("**Matriz de Correlação:**")
    corr = df_last_year.corr()
    st.write(corr)
    st.write("""
    **Análise da Matriz de Correlação:**  
    A matriz de correlação mostra as relações lineares entre as variáveis do conjunto de dados do último ano.  
    Por exemplo:
    - Uma forte correlação entre 'Open' e 'Close' indica consistência no comportamento dos preços.
    - A relação entre 'Volume' e 'Return' pode sugerir se um maior volume está associado a maiores variações percentuais.
    Essa análise é crucial para identificar interdependências entre variáveis e para fundamentar possíveis modelos preditivos.
    """)
    
    st.header("3. Aplicação de Distribuições Probabilísticas (Último Ano)")
    st.write("""
    Utilizando somente os dados do último ano, aplicamos duas distribuições:
    - **Normal:** Para modelar os **Retornos Diários**, permitindo avaliar a simetria e a volatilidade dos movimentos de preços.
    - **Poisson:** Para modelar a contagem semanal de dias em que o preço fechou acima do de abertura, ajudando a compreender a frequência desses eventos.
    """)
    
    # Distribuição Normal para os Retornos Diários com dados do último ano
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
    
    # Distribuição de Poisson para a contagem de dias de alta com dados do último ano
    st.subheader("Distribuição de Poisson - Contagem de Dias de Alta (Último Ano)")
    st.write("""
    Consideramos cada dia em que o preço de fechamento supera o de abertura como um evento de "alta".  
    Agregamos esses eventos por semana para obter a contagem semanal, que é modelada com uma distribuição de Poisson.
    """)
    df_last_year["Up_Day"] = (df_last_year["Close"] > df_last_year["Open"]).astype(int)
    df_last_year["Week"] = pd.to_datetime(df_last_year["Date"]).dt.isocalendar().week
    weekly_up_year = df_last_year.groupby("Week")["Up_Day"].sum().reset_index()
    
    from scipy.stats import poisson
    fig2, ax2 = plt.subplots()
    lam = weekly_up_year["Up_Day"].mean()
    count_values = weekly_up_year["Up_Day"].value_counts().sort_index()
    ax2.bar(count_values.index, count_values.values, alpha=0.6, color='blue', label='Dados Observados')
    x_poisson = np.arange(weekly_up_year["Up_Day"].min(), weekly_up_year["Up_Day"].max()+1)
    poisson_probs = poisson.pmf(x_poisson, lam) * len(weekly_up_year)
    ax2.plot(x_poisson, poisson_probs, 'ro-', label='Distribuição Poisson')
    ax2.set_title(f"Distribuição de Poisson para Dias de Alta Semanais (Último Ano)\n(lambda = {lam:.2f})")
    ax2.set_xlabel("Número de Dias de Alta por Semana")
    ax2.set_ylabel("Frequência")
    ax2.legend()
    st.pyplot(fig2)
    


# Executar o app:
# No terminal, rode: streamlit run curriculo.py