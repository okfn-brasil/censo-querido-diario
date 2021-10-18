# -*- coding: utf-8 -*-

import pandas as pd

def exporta(dados, nome):
    dados.to_csv(path_or_buf="./%s.csv" %(nome), encoding='UTF-8')


def formatos_publicacao(df):
    aux_abs = df["tipo_arquivo"].value_counts().sort_values()
    exporta(aux_abs, "Formatos-publicacao")


def publica_HTML(df):
    municipios_html = df[df['tipo_arquivo'] == 'HTML'].filter(items=['municipio', 'data_inicial']).sort_values(by='data_inicial').head(10)
    exporta(municipios_html, "HTML")


def formatos_UF(df):
    df_uf = df.groupby(["UF", "tipo_arquivo"])["municipio"].nunique()
    df_uf = df_uf.reset_index().pivot('UF', 'tipo_arquivo', 'municipio')
    df_uf = df_uf.fillna(0).astype(int)
    exporta(df_uf, "Formatos-UF")
