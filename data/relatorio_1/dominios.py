
# -*- coding: utf-8 -*-

import pandas as pd

def exporta(dados, nome):
    dados.to_csv(path_or_buf="./%s.csv" %(nome), encoding='UTF-8')
    
    
def dominio(df):
    temp = df['dominio'].value_counts().sort_values(ascending=False)
    exporta(temp, "Dominio")       

    
def dominio_UF(df):
    temp = df.groupby(["dominio"])["UF"].nunique().sort_values(ascending=False)           # total de estados atendidos pelo domínio
    exporta(temp, "Dominio_UF")   

    
def publica_HTML(df):
    municipios_html = df[df['tipo_arquivo'] == 'HTML'].filter(items=['municipio', 'UF', 'eh_capital','dominio'])
    exporta(municipios_html, "HTML_dominio")
    
    
def is_gov(df):
    govern = df[df["fonte"].str.contains("gov.br", na=False)].shape[0]
    n_govern = df.shape[0] - govern
    temp = pd.DataFrame({"Fonte Governamental": [govern], "Fonte não-Governamental": [n_govern]}).transpose()
    temp.columns = ['Quantidade']
    exporta(temp, "PortaisGOV")
    
    
def is_https(df):
    https = df[df["fonte"].str.contains("https", na=False)].shape[0]
    http = df.shape[0] - https
    temp = pd.DataFrame({"HTTP": [http], "HTTPS": [https]}).transpose()
    temp.columns = ['Quantidade']
    exporta(temp, "HTTPs")

    
def qntd_fontes(df):
    um = df[df['qtd_fontes'] == 1].shape[0]
    dois = df[df['qtd_fontes'] == 2].shape[0]
    tres = df[df['qtd_fontes'] == 3].shape[0]
    temp = pd.DataFrame({"1": [um], "2": [dois], "3": [tres]}).transpose()
    temp.columns = ["Contagem de cidades"]
    exporta(temp, "quantidade-fontes")
