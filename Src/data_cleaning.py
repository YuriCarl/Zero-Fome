import pandas as pd
import numpy as np
from pathlib import Path
import inflection 


# =========================================================
# FUNÇÕES E DICIONÁRIOS AUXILIARES (Anexados)
# =========================================================

COUNTRIES = {
    1: "India", 14: "Australia", 30: "Brazil", 37: "Canada", 94: "Indonesia",
    148: "New Zeland", 162: "Philippines", 166: "Qatar", 184: "Singapure",
    189: "South Africa", 191: "Sri Lanka", 208: "Turkey", 214: "United Arab Emirates",
    215: "England", 216: "United States of America",
}

COLORS = {
    "3F7E00": "darkgreen", "5BA829": "green", "9ACD32": "lightgreen",
    "CDD614": "orange", "FFBA00": "red", "CBCBC8": "darkred", "FF7800": "darkred",
}

def country_name(country_id):
    return COUNTRIES.get(country_id, "Unknown")

def create_price_type(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

def color_name(color_code):
    return COLORS.get(color_code, "Unknown")

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

# =========================================================
# FUNÇÃO DE ETL
# =========================================================

def data_cleaning():
    # EXTRACT
    ROOT_DIR = Path(__file__).parent.parent
    DATA_PATH = ROOT_DIR / "Data" / "dataset.csv"

    try:
        df = pd.read_csv(DATA_PATH)
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")
        return None

    # TRANSFORM
    
    # 1. Renomear colunas primeiro usando a função fornecida
    df = rename_columns(df)
    
    # 2. Limpeza básica (espaços e nulos)
    df.columns = df.columns.str.strip()
    df = df.dropna(how='all')
    
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    # 3. APLICAÇÃO DAS NOVAS CATEGORIZAÇÕES
    
    if 'country_code' in df.columns:
        df['country_name'] = df['country_code'].apply(country_name)
        
    if 'price_range' in df.columns:
        df['price_type'] = df['price_range'].apply(create_price_type)
        
    if 'rating_color' in df.columns:
        df['color_name'] = df['rating_color'].apply(color_name)
        
    if 'cuisines' in df.columns:
        # Pega apenas o primeiro tipo de culinária
        df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: str(x).split(",")[0])

    # 4. Continuação da limpeza numérica e duplicados
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    # LOAD
    return df

if __name__ == '__main__':
    df_clean = data_cleaning()
    if df_clean is not None:
        print(df_clean.head())