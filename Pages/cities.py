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


st.title('🏙️ Dashboard - Visão Cidades')


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
    fig11 = pt.top_10_cities_by_restaurants(df)
    st.plotly_chart(fig11, use_container_width=True)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        fig12 = pt.top_7_citys_rating_4 (df)
        st.plotly_chart(fig12, use_container_width=True)

    with col2:  
        fig13 = pt.top_7_citys_rating_2_5 (df)
        st.plotly_chart(fig13, use_container_width=True)

with st.container():
    fig14 = pt.top_10_cities_by_cuisines(df)
    st.plotly_chart(fig14, use_container_width=True)