import pandas as pd
import numpy as np
from urllib.parse import urlparse


import auxilia_tratamento_fontes

def recorta_perfil(df):
    ''' (DataFrame) -> DataFrame
    Seleciona as cidades cuja população tem a partir de 100 mil habitantes '''
    return df.loc[df["populacao_2020"] >= 100000]


def substitui_sem_diario(df):
    '''(DataFrame) -> DataFrame
    Atualiza os dados guardados em 'is_online', 'data_inicial', 'tipo_arquivo' em 4 cidades para 'Indefinido'.
    '''
    cidades=["Viamão (RS)", "Rio Grande (RS)", "Tubarão (SC)", "Tatuí (SP)"]
    variaveis=["is_online", "data_inicial", "tipo_arquivo", 'fonte_1', 'fonte_2', 'fonte_3', 'fonte_4']
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


def trata_datas(df):
    ''' (DataFrame) -> DataFrame
    Trata a variavel data_inicial e cria novas variaveis para mes e ano para melhor processamento'''
    # substitui o formato dos dados da variavel de datas
    df['data_inicial']= pd.to_datetime(df['data_inicial'], format='%Y-%m-%d',errors='coerce')

    # cria nova variavel para ano
    df['ano_inicial'] = pd.to_numeric(df['data_inicial'].dt.strftime('%Y'))
    df['ano_inicial'] = df['ano_inicial'].replace({np.nan: 'Indefinido'})

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


def trata_fontes(fontes):
    ''' (DataFrame) -> DataFrame
    Percorre as variaveis de fontes e cria um novo DataFrame com entradas para cada fonte e não para cada cidade
    '''
    # cria conjunto de dados por fonte
    fontes = auxilia_tratamento_fontes.fontes_melted(fontes) 

    # cria a variavel dominio para a lista de fontes
    fontes['dominio'] = fontes['fonte'].apply(lambda url: urlparse(url).netloc)

    # cria a variavel path
    fontes = auxilia_tratamento_fontes.extrai_path(fontes)
                    
    '''
    A partir da variavel path, é possivel perceber que apenas 20 delas se repetem
    Essas 20 são classificadas manualmente a seguir
    '''
    referencia_classificacao = auxilia_tratamento_fontes.cria_classificacao()
    
    #utiliza a referencia_classificacao para classificar as demais fontes
    fontes = auxilia_tratamento_fontes.classifica_fontes(fontes, referencia_classificacao)
    
    # remove stopwords (e, de), remove caracteres especiais, acentos, fazer o nome ficar em caixa baixa
    fontes = auxilia_tratamento_fontes.corrige_palavras(fontes)
    
    #lida com o conflito de trechos de palavras estarem contidas em outras (diaRIOs, reSULtados)
    fontes = auxilia_tratamento_fontes.conflito_em_palavras(fontes)
    
    #atualiza a referencia de classificacao com as novas fontes municipais encontradas
    referencia_classificacao['fontes_municipio'].extend(fontes[fontes['municipio_has_name_word_in_fonte']]['fonte_dominio_path'].to_list())
    
    #classifica os municipios que sao de fonte compartilhada
    fontes_compartilhadas = referencia_classificacao["fontes_associacao"] + referencia_classificacao["fontes_estado"] + referencia_classificacao["fontes_uniao"]
    fontes["fontes_compartilhadas"] = fontes['fonte'].apply(lambda fonte: any([fc in fonte for fc in fontes_compartilhadas]))
    
    #classifica as fontes restantes, as não compartilhadas
    referencia_classificacao = auxilia_tratamento_fontes.estende_classificacao(referencia_classificacao)
    
    #classifica fontes
    fontes = auxilia_tratamento_fontes.classifica_fontes(fontes, referencia_classificacao)
    
    #classifica fontes gov
    fontes['fonte_governamental'] = fontes['dominio'].str.contains('\.gov')
    
    return fontes


