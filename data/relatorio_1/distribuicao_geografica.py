#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:53:50 2021

@author: trevo
"""

def exporta(dados, nome):
    dados.to_csv(path_or_buf="./%s.csv" %(nome), encoding='UTF-8')
    
    
# DISTRIBUIÇÃO GEOGRÁFICA
def municipios_UF(df):
    municipios_por_uf = df['UF'].value_counts().sort_values()
    exporta(municipios_por_uf, "Municipios-por-UF")
      
def municipios_regiao(df):
    municipios_por_regiao = df['regiao'].value_counts().sort_values()
    exporta(municipios_por_regiao, "Municipios-por-regiao")
   
