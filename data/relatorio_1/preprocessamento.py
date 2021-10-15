import pandas as pd
import numpy as np
from urllib.parse import urlparse
from urllib.parse import urlsplit
from functools import reduce

def recorta_perfil(df):
    ''' (None) -> None
    Seleciona as cidades cuja população tem a partir de 100 mil habitantes '''    
    return df.loc[df["populacao_2020"] >= 100000]
  
    
def substitui_sem_diario(df):
    '''(DataFrame) -> DataFrame 
    Atualiza os dados guardados em 'is_online', 'data_inicial', 'tipo_arquivo' em 4 cidades para 'Indefinido'.
    '''
    cidades=["Viamão (RS)", "Rio Grande (RS)", "Tubarão (SC)", "Tatuí (SP)"]
    variaveis=["is_online", "data_inicial", "tipo_arquivo"]
    colunas = df.columns.to_list()
    
    for cidade in cidades:
        linha = df.index[df['municipio'] == cidade]
        for variavel in variaveis:
            coluna = colunas.index(variavel)      
            df.iloc[linha, coluna] = "Indefinido"
    return df
  

def substitui_formato(df):
    '''(DataFrame) -> DataFrame
    Esta função recebe um conjunto de dados e altera, na variável 'tipo_arquivo', as aparições de'Outro formato' para 'Imagem (PNG e JPEG)' 
    '''
    df['tipo_arquivo'] = df['tipo_arquivo'].replace(['Outro formato'],'Imagem (PNG ou JPEG)')
    return df
  

def remove_variaveis(df):
    ''' (DataFrame) -> Dataframe
    Remove as variaveis IBGE, validacao, navegacao, observacoes
    '''
    return df.drop(columns=['IBGE', 'validacao', 'navegacao', 'observacoes'])
  

def extract_domain_and_path(df):
    '''(DataFrame) -> DataFrame
    (((explicar o que isso faz)))
    '''
    return df.apply(lambda url: urlsplit(url)[1:3]).str.join('')
  

def remove_www(df):
    '''(DataFrame) -> DataFrame
    (((explicar o que isso faz)))
    '''
    return df.str.replace('^www\d?\.', '')
  

def trata_fontes(df):
    ''' (DataFrame) -> DataFrame
    Percorre as variaveis de fontes e cria um novo DataFrame com entradas para cada fonte e não para cada cidade
    '''   
    fonte_melted = df.melt(value_vars=['fonte_1', 'fonte_2', 'fonte_3', 'fonte_4'], value_name='fonte', ignore_index=False)
    df = df.join(fonte_melted['fonte']).drop(columns=['fonte_1', 'fonte_2', 'fonte_3', 'fonte_4'])
    df = df[df['fonte'] != 'None'].reset_index(drop=True)
     
    # cria a variavel dominio para a lista de fontes
    df['dominio'] = df['fonte'].apply(lambda url: urlparse(url).netloc)
    
    # cria a variavel path
    df['fonte_dominio_path'] = df['fonte'] \
                .pipe(extract_domain_and_path) \
                .pipe(remove_www) \
                .str.rstrip('/')  
    return df
  

def trata_datas(df):
    ''' (DataFrame) -> DataFrame
    Trata a variavel data_inicial e cria novas variaveis para mes e ano para melhor processamento'''    
    # substitui o formato dos dados da variavel de datas
    df['data_inicial']= pd.to_datetime(df['data_inicial'], format='%Y-%m-%d',errors='coerce')
    
    # cria novas variaveis para ano e mes
    df['ano_inicial'] = pd.to_numeric(df['data_inicial'].dt.strftime('%Y'))
    df['ano_inicial'] = df['ano_inicial'].replace({np.nan: 'Indefinido'})

    df['mes_inicial'] = pd.to_numeric(df['data_inicial'].dt.strftime('%m'))
    df['mes_inicial'] = df['mes_inicial'].replace({np.nan: 'Indefinido'})
    
    # substitui os NaN por Indefinido
    df['data_inicial'] = df['data_inicial'].replace({np.nan: 'Indefinido'})

    return df
  

def conta_fontes(df, df_aux):
    ''' (DataFrame) -> DataFrame
    Utiliza o dataframe (df_aux) de apoio para contar quantas fontes de publicacao de diarios cada cidade tem
    '''
    s = df_aux['municipio'].value_counts().to_frame()
    s.columns=["qtd_fontes"]
    df = df.join(s, on = 'municipio', how='left')
    return df
    
