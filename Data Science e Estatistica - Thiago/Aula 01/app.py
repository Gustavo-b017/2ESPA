# python -m streamlit run app.py
# streamlit run app.py
# pip install streamlit
# pip install openpyxl

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Marketing Analytics")
st.text("Esse dashboard res")

uploaded_file = st.file_uploader("Carregue seu arquivo aqui")

if uploaded_file:
  df = pd.read_excel(uploaded_file)
  st.write(df.describe())
  st.header('Data Headar')
  st.write(df.head())

  # criando os eixos
  fig, ax = plt.subplots(1, 1)
  
  # Filtrando os dados
  reel_data = df[df['Post type'] == 'IG reel']
  image_data = df[df['Post type'] == 'IG image']
  carousel_data = df[df['Post type'] == 'IG carousel']
  
  # Plotando os dados
  ax.scatter(reel_data['Reach'], reel_data['Likes'], color='red', label='IG reel')
  ax.scatter(image_data['Reach'], image_data['Likes'], color='green', label='IG image')
  ax.scatter(carousel_data['Reach'], carousel_data['Likes'], color='blue', label='IG carousel')
  
  ax.set_xlabel('Alcance')
  ax.set_ylabel('Curtidas')
  ax.legend()

  st.pyplot(fig)