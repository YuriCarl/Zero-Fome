import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import folium
import sys
import os
import streamlit as st


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


st.title('🍽️ Dashboard - Visão Culinárias')

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

top_n = st.sidebar.slider(
    "Selecione a quantidade de Restaurantes que deseja visualizar", 1, 20, 10
    )

# Filtros Sidebar - Culinarias
cuisines = st.sidebar.multiselect(
    "Escolha as Culinárias que Deseja visualizar os Restaurantes",
    df.loc[:, "cuisines"].unique().tolist(),
    default=[ "BBQ", "Japanese", "Brazilian", "Arabian", "American", "Italian",],)

# Aplicação de filtro de culinarias
cuisine_opcoes = cuisines
linhas_selecionadas = df['cuisines'].isin(cuisine_opcoes) # Filtro Culinarias
df = df.loc[linhas_selecionadas, :]

# ========================================
# Dashboard
# ========================================

with st.container():
    st.markdown("## Top 10 Restaurantes")
    df_top10 = pt.top10_restaurantes_list(df)
    st.dataframe(df_top10)

with st.container(): 
    col1, col2 = st.columns(2)

    with col1:
        fig15 = pt.top10_best_cuisines_by_rating (df)
        st.plotly_chart(fig15, use_container_width=True)

    with col2:
        fig16 = pt.top10_worst_cuisines_by_rating (df)
        st.plotly_chart(fig16, use_container_width=True)