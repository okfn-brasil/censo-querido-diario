#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:26:34 2021

@author: trevo
"""

def exporta(dados, nome):
    dados.to_csv(path_or_buf="./%s.csv" %(nome), encoding='UTF-8')

def um_diario_antigo(df):
    df = df[df['data_inicial'] != 'Indefinido']
    ## Cidade com diário mais antigo e primeira data de publicacao
    diario_antigo = df['data_inicial'].min()
    cidade_antiga = df[df['data_inicial'] == diario_antigo]
    
    print("a data do diário mais antigo é:" , diario_antigo, "do municipio de", cidade_antiga['municipio'])
    
def diarios_antigos(df):
    df = df[df['data_inicial'] != 'Indefinido']
    top = df.sort_values('data_inicial', ascending=True).filter(items=['municipio', 'regiao', 'populacao_2020','eh_capital','data_inicial']).head(10)
    exporta(top,"TOP10-cidades-antigas")

    
def um_diario_novo(df):
    df = df[df['data_inicial'] != 'Indefinido']
    ## Cidade com diário mais recente e primeira data de publicacao
    diario_recente = df['data_inicial'].max()
    cidade_recente = df[df['data_inicial'] == diario_recente]
    print("a data do diário mais recente é:" , diario_recente, "do municipio de", cidade_recente['municipio'])


def diarios_novos(df):
    df = df[df['data_inicial'] != 'Indefinido']
    bottom = df.sort_values('data_inicial', ascending=False).filter(items=['municipio', 'regiao', 'populacao_2020','eh_capital','data_inicial']).head(10)
    exporta(bottom,"TOP10-cidades-recentes")


def dist_anual(df):
    df = df['ano_inicial'].value_counts()
    exporta(df,"distribuicao_anual")

def lista_anos(df):
    df = df[['municipio', 'ano_inicial']]
    exporta(df, "ano_de_publicacao-lista_completa")
    


'''
def periodo_publicacao(df):
    
municipios['UF'].unique()


nordeste = municipios[municipios['regiao'] == 'Região Nordeste']
norte = municipios[municipios['regiao'] == 'Região Norte']
sul = municipios[municipios['regiao'] == 'Região Sul']
sudeste = municipios[municipios['regiao'] == 'Região Sudeste']
centro_oeste = municipios[municipios['regiao'] == 'Região Centro-Oeste']

nordeste['ano_inicial'].describe()

Criar um dataframe com as medidas de posição (quartis) para elaborar uma visualisação.

regioes_lista = [nordeste, norte, sul, sudeste, centro_oeste]
valor_minimo =[]
valor_maximo = []
primeiro_quartil =[]
segundo_quartil =[]
terceiro_quartil =[]


for regiao in (regioes_lista):
    quartil = regiao['ano_inicial'].quantile(q=0.25)
    primeiro_quartil.append(quartil)
    
for regiao in regioes_lista:
    quartil = regiao['ano_inicial'].quantile(q=0.50)
    segundo_quartil.append(quartil)

for regiao in regioes_lista:
    quartil = regiao['ano_inicial'].quantile(q=0.75)
    terceiro_quartil.append(quartil)

for regiao in regioes_lista:
    min = regiao['ano_inicial'].min()
    valor_minimo.append(min)

for regiao in regioes_lista:
    max = regiao['ano_inicial'].max()
    valor_maximo.append(max)


# Convertendo em tupla para "travar" os valores
valor_minimo = tuple(valor_minimo)
valor_maximo = tuple(valor_maximo)
primeiro_quartil = tuple(primeiro_quartil)
segundo_quartil = tuple(segundo_quartil)
terceiro_quartil = tuple(terceiro_quartil)

# Dados para o parâmetro "data" para transformar em DataFrame
dados_regioes = {
  
    'Mais antigo':valor_minimo,
    'Mais recente':valor_maximo,
    '1º quartil' : primeiro_quartil,
    '2º quartil' : segundo_quartil,
    '3º quartil' : terceiro_quartil
}


dados_regioes

df_comparativo_regioes = pd.DataFrame(data=dados_regioes,
                                      index=('nordeste', 'norte', 'sul', 'sudeste', 'centro-oeste'))

df_comparativo_regioes
'''
