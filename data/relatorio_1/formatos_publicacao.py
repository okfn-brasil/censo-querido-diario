import pandas as pd

def exporta(dados, nome):
    dados.to_csv(f"./resultados/{nome}.csv", encoding='UTF-8')


def formatos_publicacao(df):
    aux_abs = df["tipo_arquivo"].value_counts().sort_values()
    exporta(aux_abs, "(b) Formatos-publicacao")


def publica_html(df):
    municipios_html = df[df['tipo_arquivo'] == 'HTML'][['municipio', 'data_inicial']].sort_values('data_inicial').head(10)
    exporta(municipios_html, "(b) TOP10-HTML")
