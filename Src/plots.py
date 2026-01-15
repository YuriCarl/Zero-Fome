import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import os

# ========================================
# Carregamento de dados
# ========================================

import Src.data_cleaning as dc

df = dc.data_cleaning()


# ========================================
# Funções da Página Geral
# ========================================

def unique_restaurants(df): # Número de restaurantes únicos
    unique_restaurant_count = df['restaurant_name'].nunique()

    return unique_restaurant_count

def unique_countries(df): # Número de países únicos
    unique_country_count = df['country_code'].nunique() 

    return unique_country_count

def unique_cities(df): # Número de cidades únicas
    unique_city_count = df['city'].nunique() 

    return unique_city_count

def total_reviews(df): # Total de avaliações
    total_review_count = df['votes'].count() 

    return total_review_count

def total_cousines(df): # Total de culinárias
    total_cuisine_count = df['cuisines'].nunique() 

    return total_cuisine_count

def restaurant_location(df): # Mapa de localização dos restaurantes
    # 1. Configuração do mapa base centralizado
    # Usando a média das coordenadas do df
    map_center = [df['latitude'].mean(), df['longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=2, control_scale=True)

    # 2. Criação do Cluster de Marcadores
    marker_cluster = MarkerCluster().add_to(m)

    # 3. Iteração para adicionar os pontos individuais
    for index, location_info in df.iterrows():
        
        # Coleta a cor tratada na limpeza
        color = location_info['color_name']
        
        # HTML customizado para o Popup
        popup_html = f"""
            <b>{location_info['restaurant_id']}</b><br>
            Nota: {location_info['aggregate_rating']}/5.0<br>
            Culinária: {location_info['cuisines']}<br>
            Preço médio: {location_info['average_cost_for_two']} ({location_info['currency']})
        """
        
        # Adiciona o marcador ao CLUSTER
        folium.Marker(
            location=[location_info['latitude'], location_info['longitude']],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(color=color, icon='home', prefix='fa') # Usa a cor da nota
        ).add_to(marker_cluster)

    # 4. Exibição do mapa
    return folium_static(m, width=1024, height=600)  # Exibição mapa


# ========================================
# Funções da Página País
# ========================================

def count_restaurants_by_country(df): # Contagem de restaurantes registrados por país
    columns = ['country_name', 'restaurant_id']
    count_country_restaurants = df.loc[:, columns].groupby('country_name').nunique().reset_index().sort_values('restaurant_id', ascending=False)
    fig7 = px.bar(count_country_restaurants, 
                  x='country_name', 
                  y='restaurant_id', 
                  text='restaurant_id',
                  color='country_name',
                  title='Número de Restaurantes por País',
                  labels= {'country_name': 'Países',
                           'restaurant_id': 'Número de Restaurantes'})
    return fig7

def citys_by_country(df): # Contagem de cidades registadas por país
    columns = ['country_name', 'city']
    count_citys_by_country = df.loc[:, columns].groupby('country_name').nunique().reset_index().sort_values('city', ascending=False)
    fig8 = px.bar(count_citys_by_country, 
                  x='country_name', 
                  y='city',
                  text='city',
                  color='country_name',
                  title='Número de Cidades por País',
                  labels= {'country_name': 'Paises',
                           'city': 'Número de Cidades'})
    return fig8

def average_rating_by_country(df): # Média de avaliações por país
    columns = ['country_name', 'aggregate_rating']
    average_rating_country = df.loc[:, columns].groupby('country_name').mean().round(2).reset_index().sort_values('aggregate_rating', ascending=False)
    fig9 = px.bar(average_rating_country, 
                  x='country_name', 
                  y='aggregate_rating',  
                  text='aggregate_rating',
                  text_auto=".2f",
                  color='country_name',
                  title='Média de Avaliações por País',
                  labels= {'country_name': 'Países',
                           'aggregate_rating': 'Média de Avaliações'})
    return fig9

def mean_cost_dishes_by_country(df): # Média de custo de prato para dois por páis
    columns = ['country_name', 'average_cost_for_two']
    average_cost_country = df.loc[:, columns].groupby('country_name').mean().round(2).reset_index().sort_values('average_cost_for_two', ascending=False)
    fig10 = px.bar(average_cost_country, 
                  x='country_name', 
                  y='average_cost_for_two',
                  text='average_cost_for_two',
                  text_auto=".2f",
                  color='country_name',
                  title='Média de Custo de Prato para Dois por País',
                  labels= {'country_name': 'Países',
                           'average_cost_for_two': 'Média de Custo para Dois'})
    return fig10


# ========================================
# Funções da Página Cidades
# ========================================

def top_10_cities_by_restaurants(df): # Top 10 cidades com mais restaurantes registrados
    columns = ['city', 'restaurant_id']
    top_10_citys = df.loc[:, columns].groupby('city').nunique().reset_index().sort_values('restaurant_id', ascending=False).head(10)
    fig11 = px.bar(top_10_citys, 
                  x='city', 
                  y='restaurant_id',
                  text='restaurant_id',
                  title='Top 10 Cidades com Mais Restaurantes Registrados',
                  labels= {'city': 'Cidades',
                           'restaurant_id': 'Número de Restaurantes'})
    return fig11

def top_7_citys_rating_4 (df): # Top 7 cidades com restaurantes com média de avaliação acima de 4
    countries = df["country_name"].unique().tolist()
    top_7cities_rating_4 = (df.loc[(df["aggregate_rating"] >= 4) & (df["country_name"].isin(countries)),["restaurant_id", "country_name", "city"]].groupby(["country_name", "city"]).count().sort_values(["restaurant_id", "city"], ascending=[False, True]).reset_index().head(7))
    fig12 = px.bar(top_7cities_rating_4,
           x='city',
           y='restaurant_id', 
           text='restaurant_id',
           color='country_name',
           title='Top 7 Cidades com Restaurantes com média de avaliação acima de 4',
           labels={'city': 'Cidade',
                   'restaurant_id': 'Quantidade de Restaurantes', 
                   'country_name': 'País'})
    return fig12
    
def top_7_citys_rating_2_5 (df): # Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5
    countries = df["country_name"].unique().tolist()
    top_7cities_rating_2_5 = (df.loc[(df["aggregate_rating"] <= 2.5) & (df["country_name"].isin(countries)),["restaurant_id", "country_name", "city"]].groupby(["country_name", "city"]).count().sort_values(["restaurant_id", "city"], ascending=[False, True]).reset_index().head(7))
    fig13 = px.bar(top_7cities_rating_2_5,
           x='city',
           y='restaurant_id',
           text='restaurant_id',
           color='country_name',
           title='Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5',
           labels={'city': 'Cidade',
                   'restaurant_id': 'Quantidade de Restaurantes', 
                   'country_name': 'País'})
    return fig13

def top_10_cities_by_cuisines(df): # Top 10 cidades com maior variedade de culinárias
    columns = ['city', 'cuisines', 'country_name']
    top_10_citys_cuisines = df.loc[:, columns].groupby(['city', 'country_name']).nunique().reset_index().sort_values('cuisines', ascending=False).head(10)
    fig14 = px.bar(top_10_citys_cuisines, 
                  x='city', 
                  y='cuisines',  
                  color='country_name',
                  text='cuisines',
                  title='Top 10 Cidades com Maior Variedade de Culinárias',
                  labels= {'city': 'Cidades',
                           'cuisines': 'Número de Culinárias'})
    return fig14


# ========================================
# Funções da Página Culinárias
# ========================================

def top10_restaurantes_list(df): # Top 10 restaurantes mais bem avaliados

    cols = [
        "restaurant_id",
        "restaurant_name",
        "country_name",
        "city",
        "cuisines",
        "average_cost_for_two",
        "aggregate_rating",
        "votes",
    ]

    lines = (
        df["cuisines"].notna() &
        df["country_name"].notna()
    )

    top10_restaurantes = (
        df.loc[lines, cols]
        .sort_values(
            ["aggregate_rating", "restaurant_id"],
            ascending=[False, True]
        )
        .head(10)
    )

    return top10_restaurantes

def top10_best_cuisines_by_rating(df): # Top 10 melhores culinárias por avaliação média
    lines = (
        df["cuisines"].notna() &
        df["country_name"].notna()
    )
    grouped_df = (df.loc[lines, ["aggregate_rating", "cuisines"]].groupby("cuisines").mean().round(2).sort_values("aggregate_rating", ascending=False).reset_index().head(10))

    fig15 = px.bar(
        grouped_df.head(10),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title="Top 10 Melhores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação Média",
        },
    )

    return fig15

def top10_worst_cuisines_by_rating(df): # Top 10 piores culinárias por avaliação média
    lines = (
        df["cuisines"].notna() &
        df["country_name"].notna()
    )
    grouped_df = (df.loc[lines, ["aggregate_rating", "cuisines"]].groupby("cuisines").mean().round(2).sort_values("aggregate_rating").reset_index().head(10))

    fig16 = px.bar(
        grouped_df.head(10),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title="Top 10 Piores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação Média",
        },
    )

    return fig16