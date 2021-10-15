#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:58:59 2021

@author: trevo
"""
import pandas as pd 

def exporta(dados, nome):
    dados.to_csv(path_or_buf="./%s.csv" %(nome), encoding='UTF-8')
    

# FORMATOS DE ARQUIVOS
def formatos_publicacao(df):
    # absoluto
    aux_abs = df["tipo_arquivo"].value_counts().sort_values()
    exporta(aux_abs, "Formatos-publicacao")
    # porcentagem
    aux_porc = aux_abs/df.shape[0]*100
    exporta(aux_porc, "Formatos-publicacao-(%)")
    # tabela        
    temp = pd.concat([aux_abs, aux_porc], axis=1)
    temp.columns=['formato', '%']
    exporta(temp, "Formatos-publicacao-(tabela)")


def publica_HTML(df):
    municipios_html = df[df['tipo_arquivo'] == 'HTML'].filter(items=['municipio', 'UF', 'eh_capital','dominio'])
    exporta(municipios_html, "HTML")
       
def formatos_capitais(df):
    # tabela
    capitais = df[df['eh_capital']].filter(items=['municipio', 'tipo_arquivo'])
    exporta(capitais, "Formatos-capitais-(tabela)")
    # absoluto
    capitais = capitais['tipo_arquivo'].value_counts()
    exporta(capitais, "Formatos-capitais")
    # porcentagem
    capitais = capitais/capitais.sum()*100
    exporta(capitais, "Formatos-capitais-(%)")
    

        
def formatos_UF(df):
    df_uf = df.groupby(["UF", "tipo_arquivo"])["municipio"].nunique()
    df_uf = df_uf.reset_index().pivot('UF', 'tipo_arquivo', 'municipio')
    df_uf = df_uf.fillna(0).astype(int)
    exporta(df_uf, "Formatos-UF")
    
    # porcentagem
    df_uf = df_uf/df.shape[0]*100
    exporta(df_uf, "Formatos-UF-(%)")
    


