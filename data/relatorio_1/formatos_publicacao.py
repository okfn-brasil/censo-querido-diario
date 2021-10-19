import pandas as pd

def exporta(dados, nome):
    dados.to_csv(f"./resultados/{nome}.csv", encoding='UTF-8')


def formatos_publicacao(df):
    aux_abs = df["tipo_arquivo"].value_counts().sort_values()
    exporta(aux_abs, "(b) Formatos-publicacao")


def publica_html(df):
    municipios_html = df[df['tipo_arquivo'] == 'HTML'][['municipio', 'data_inicial']].sort_values('data_inicial').head(10)
    exporta(municipios_html, "(b) TOP10-HTML")


def formatos_por_uf(df):
    df_uf = df.groupby(["UF", "tipo_arquivo"])["municipio"].nunique()
    df_uf = df_uf.reset_index().pivot('UF', 'tipo_arquivo', 'municipio')
    df_uf = df_uf.fillna(0).astype(int)
    exporta(df_uf, "(b) Formatos-UF")
