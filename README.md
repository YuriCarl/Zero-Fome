
# Zero Fome

## 📋 Descrição

Este projeto apresenta uma análise detalhada dos dados da marketplace de restaurantes Fome Zero. O objetivo principal é fornecer insights estratégicos para o CEO da empresa, permitindo uma visão holística sobre os restaurantes cadastrados, países atendidos e performance das culinárias.

A Fome Zero é um marketplace que conecta clientes a restaurantes globalmente. Para entender melhor o crescimento e a qualidade do serviço, foi desenvolvida uma solução de visualização de dados que responde a perguntas fundamentais sobre:

- Crescimento da base de restaurantes e cidades.
- Avaliação média por país e culinária.
- Distribuição geográfica das unidades.
- Custos médios de pratos para duas pessoas.

### 🎯 Tecnologias utilizadas

O projeto foi construído inteiramente em Python, utilizando as seguintes bibliotecas:

- Manipulação de Dados: pandas, numpy, inflection, pathlib.
- Visualização Interativa: plotly, plotly-express.
- Mapas: folium, streamlit-folium.
- Interface Web (Dashboard): streamlit.

### 🚀 Pricipais Insights

Com base no dashboard, podemos observar que:

- A Inglaterra possui a maior concentração de restaurantes na base atual, mas o Brasil apresenta um custo médio para dois significativamente variado dependendo da cidade.
- Cidades como Birmingham e Brasília lideram o ranking de volume de registros.
- Culinárias como BBQ e Japanese estão entre as melhores avaliadas na plataforma.

## Pré-requisitos

Os pré-requisitos para o uso do código são a instalação das bibliotecas listadas abaixo: 

- pandas
- numpy
- plotly
- plotly-express
- folium
- streamlit
- streamlit-folium
- inflection 
- pathlib

## Utilização

### Clone o repositório:

```bash
git clone https://github.com/YuriCarl/Zero-Fome
```
```bash
cd zero-fome
```

### Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execute o Streamlit:

```bash
streamlit run ./main.py
```

## 📁 Estrutura do Projeto

```
zero-fome/
├── Src/
├── Data/
├── Pages/
└── README.md
└── requirements.txt
```

## 📧 Contato

- yurioli.dev@gmail.com
- https://www.linkedin.com/in/yurioli/

---
