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