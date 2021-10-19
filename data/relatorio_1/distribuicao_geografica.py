def exporta(dados, nome):
    dados.to_csv(f"./resultados/{nome}.csv", encoding='UTF-8')

# DISTRIBUIÇÃO GEOGRÁFICA
def municipios_por_uf(df):
    municipios_por_uf = df['UF'].value_counts().sort_values()
    exporta(municipios_por_uf, "(a) Municipios-por-UF")

def municipios_por_regiao(df):
    municipios_por_regiao = df['regiao'].value_counts().sort_values()
    exporta(municipios_por_regiao, "(a) Municipios-por-regiao")
