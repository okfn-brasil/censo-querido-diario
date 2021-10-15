#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 12:18:09 2021

@author: trevo
"""
import pandas as pd

def exporta(dados, nome):
    dados.to_csv(path_or_buf="./%s.csv" %(nome), encoding='UTF-8')
    
# FONTES DE PUBLICACAO
    
def dominio(df):
    temp = df['dominio'].value_counts().sort_values(ascending=False)
    exporta(temp, "Dominio")
    #porcentagem
    temp = (temp/temp.shape[0]*100)
    exporta(temp, "Dominio-(%)")
    
    
def dominio_maior_um(df):
    temp = df['dominio'].value_counts().sort_values(ascending=False)
    aux = temp[temp > 1]
    exporta(aux, "Dominio_maior-um")
    #porcentagem
    aux = (aux/temp.shape[0]*100).sort_values(ascending=False)
    exporta(aux, "Dominio_maior-um-(%)")    
    

def dominio_UF(df):
    temp = df.groupby(["dominio"])["UF"].nunique().sort_values(ascending=False)           # total de estados atendidos pelo domínio
    exporta(temp, "Dominio_UF")   


def is_gov(df):
    govern = df[df["fonte"].str.contains("gov.br", na=False)].shape[0]
    n_govern = df.shape[0] - govern
    temp = pd.DataFrame({"Fonte Governamental": [govern], "Fonte não-Governamental": [n_govern]}).transpose()
    temp.columns = ['Quantidade']
    exporta(temp, "PortaisGOV")
    
    # porcentagem
    aux = temp["Quantidade"].sum()
    temp = temp/aux*100
    exporta(temp, "PortaisGOV-(%)")

def publica_HTML(df):
    municipios_html = df[df['tipo_arquivo'] == 'HTML'].filter(items=['municipio', 'UF', 'eh_capital','dominio'])
    exporta(municipios_html, "HTML_dominio")
    
def is_https(df):
    https = df[df["fonte"].str.contains("https", na=False)].shape[0]
    http = df.shape[0] - https
    temp = pd.DataFrame({"HTTP": [http], "HTTPS": [https]}).transpose()
    temp.columns = ['Quantidade']
    exporta(temp, "HTTPs")
    
    # porcentagem
    aux = temp["Quantidade"].sum()
    temp = temp/aux*100  
    exporta(temp, "HTTPs-(%)")

def qntd_fontes(df):
    um = df[df['qtd_fontes'] == 1].shape[0]
    dois = df[df['qtd_fontes'] == 2].shape[0]
    tres = df[df['qtd_fontes'] == 3].shape[0]
    temp = pd.DataFrame({"1": [um], "2": [dois], "3": [tres]}).transpose()
    temp.columns = ["Contagem de cidades"]
    exporta(temp, "quantidade-fontes")
    
    #porcentagem
    total = um + dois + tres
    temp = temp/total*100
    exporta(temp, "quantidade-fontes-(%)")
    
    #outra versao
    temp = pd.DataFrame({"1": [um], "mais": [dois + tres]}).transpose()
    temp.columns = ["Contagem de cidades"]
    exporta(temp, "quantidade-fontes-v2")
    
    #porcentagem
    temp = temp/total*100
    exporta(temp, "quantidade-fontes-v2-(%)")

def qntd_fontes_capital(df):
    df = df[df['eh_capital']]
    um = df[df['qtd_fontes'] == 1].shape[0]
    dois = df[df['qtd_fontes'] == 2].shape[0]
    tres = df[df['qtd_fontes'] == 3].shape[0]
    temp = pd.DataFrame({"1": [um], "2": [dois], "3": [tres]}).transpose()
    temp.columns = ["Contagem de capitais"]
    exporta(temp, "quantidade-fontes-capitais")
    
    #porcentagem
    total = um + dois + tres
    temp = temp/total*100
    exporta(temp, "quantidade-fontes-capitais-(%)")
    
    #outra versao
    temp = pd.DataFrame({"1": [um], "mais": [dois + tres]}).transpose()
    temp.columns = ["Contagem de capitais"]
    exporta(temp, "quantidade-fontes-v2-capitais")
    
    #porcentagem
    temp = temp/total*100
    exporta(temp, "quantidade-fontes-v2-capitais-(%)")
    
    
    
def pub_agrupamentos(df):
    fontes_associacao = [
    'diariomunicipal.com.br/famep/pesquisar',
    'diariomunicipal.sc.gov.br/site',
    'diariomunicipal.com.br/amupe/pesquisar',
    'diariomunicipal.com.br/amm-mg/pesquisar',
    'diariomunicipal.com.br/amp/pesquisar',
    'diariomunicipal.org/mt/amm/publicacoes',
    'diariomunicipal.com.br/famurs/pesquisar',
    'diariomunicipal.es.gov.br',
    'diariomunicipal.com.br/amupe',
    'diariomunicipal.com.br/aam/pesquisar']
    fontes_estado = [
        'diariooficial.rs.gov.br',
        'diariooficial.abc.go.gov.br/buscanova',
        'ioepa.com.br/pesquisa',
        'imprensaoficial.com.br/DO/BuscaDO2001Resultado_11_3.aspx',
        'jornalminasgerais.mg.gov.br',
        'pesquisa.doe.seplag.ce.gov.br/doepesquisa/sead.do',
        'ioes.dio.es.gov.br/buscanova',
        'ioerj.com.br/portal/modules/conteudoonline/busca_do.php',
        'diariooficial.ma.gov.br/public/index.xhtml']
    fontes_uniao = ['in.gov.br/consulta/-/buscar/dou']
    fontes_municipio = ['cachoeirinha.atende.net']
    
    df['is_publicado_municipio'] = df['fonte'].apply(lambda fonte: is_any_of(fonte, fontes_municipio))
    df['is_publicado_associacao'] = df['fonte'].apply(lambda fonte: is_any_of(fonte, fontes_associacao))
    df['is_publicado_estado'] = df['fonte'].apply(lambda fonte: is_any_of(fonte, fontes_estado))
    df['is_publicado_uniao'] = df['fonte'].apply(lambda fonte: is_any_of(fonte, fontes_uniao))
    
def is_any_of(text, words):
    return any([w in text for w in words])




    
        
    
    
    