import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import folium
import sys
import os
import streamlit as st
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static


# ========================================
# Carregamento de dados
# ========================================

import Src.data_cleaning as dc

df = dc.data_cleaning()


# ========================================
# Carregamento de funções
# ========================================

import Src.plots as pt


# ========================================
# Configurações da página
# ========================================


st.title('🏠 Dashboard - Visão Geral')
st.markdown('### Uma análise dos restaurantes ao redor do mundo')


# ========================================
# Sidebar
# ========================================

st.sidebar.markdown('# Filtros')

# Filtros Sidebar - Paises
countries = st.sidebar.multiselect(
    "Escolha os Paises que Deseja visualizar os Restaurantes",
    df.loc[:, "country_name"].unique().tolist(),
    default=["Brazil", "England", "Qatar", "South Africa", "Canada"],)

# Aplicação de filtro de países
pais_opcoes = countries
linhas_selecionadas = df['country_name'].isin(pais_opcoes) # Filtro Paises
df = df.loc[linhas_selecionadas, :]


# ========================================
# Dashboard
# ========================================

with st.container():
  col1, col2, col3, col4, col5 = st.columns(5)

  with col1: # Card Restaurantes Cadastrados
      pt.total_restaurantes = df['restaurant_id'].nunique()
      col1.metric(label='Restaurantes Cadastrados', value=pt.total_restaurantes, border=True)

  with col2: # Card Países Cadastrados
      pt.total_paises = df['country_name'].nunique()
      col2.metric(label='Países Cadastrados', value=pt.total_paises, border=True)

  with col3: # Card Cidades Cadastradas 
      pt.total_cidades = df['city'].nunique()
      col3.metric(label='Cidades Cadastradas', value=pt.total_cidades, border=True)

  with col4: # Card Tipos de Culinárias
      pt.total_culinarias = df['cuisines'].nunique()
      col4.metric(label='Tipos de Culinárias', value=pt.total_culinarias, border=True)

  with col5: # Card Avaliações Feitas
      pt.total_users = df['votes'].sum()
      col5.metric(label='Avaliações Feitas', value=pt.total_users, border=True)

with st.container(): # Gráfico de Barras - Restaurantes por País
    st.title('Distribuição dos Restaurantes no Mundo')
    pt.restaurant_location(df)