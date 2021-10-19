import pandas as pd

def exporta(dados, nome):
    dados.to_csv(f"./resultados/{nome}.csv", encoding='UTF-8')


def dominio(df):
    temp = df['dominio'].value_counts().sort_values(ascending=False)
    exporta(temp, "(c) Dominio")


def dominio_por_uf(df):
    temp = df.groupby(["dominio"])["UF"].nunique().sort_values(ascending=False)           # total de estados atendidos pelo domínio
    exporta(temp, "(c) Dominio_por_UF")


def eh_gov(df):
    govern = df[df["fonte"].str.contains("gov.br", na=False)].shape[0]
    n_govern = df.shape[0] - govern
    temp = pd.DataFrame({"Fonte Governamental": [govern], "Fonte não-Governamental": [n_govern]}).transpose()
    temp.columns = ['Quantidade']
    exporta(temp, "(c) PortaisGOV")


def eh_https(df):
    https = df[df["fonte"].str.contains("https", na=False)].shape[0]
    http = df.shape[0] - https
    temp = pd.DataFrame({"HTTP": [http], "HTTPS": [https]}).transpose()
    temp.columns = ['Quantidade']
    exporta(temp, "(c) HTTPs")


def quantidade_fontes(df):
    um = df[df['qtd_fontes'] == 1].shape[0]
    dois = df[df['qtd_fontes'] == 2].shape[0]
    tres = df[df['qtd_fontes'] == 3].shape[0]
    temp = pd.DataFrame({"Uma fonte": [um], "Duas fontes": [dois], "Três fontes": [tres]}).transpose()
    temp.columns = ["Contagem de cidades"]
    exporta(temp, "(c) quantidade-fontes")
