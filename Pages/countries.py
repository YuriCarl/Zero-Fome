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


st.title('🌎 Dashboard - Visão Paises')

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
    fig7 = pt.count_restaurants_by_country(df)
    st.plotly_chart(fig7, use_container_width=True)

with st.container():
    fig8 = pt.citys_by_country(df)
    st.plotly_chart(fig8, use_container_width=True)

with st.container():
    col1, col2 = st.columns(2)

    with col1: 
        fig9 = pt.average_rating_by_country(df)
        st.plotly_chart(fig9, use_container_width=True)

    with col2:
        fig10 = pt.mean_cost_dishes_by_country(df)
        st.plotly_chart(fig10, use_container_width=True)
