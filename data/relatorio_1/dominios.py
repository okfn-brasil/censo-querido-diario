import pandas as pd

def exporta(dados, nome):
    dados.to_csv(f"./resultados/{nome}.csv", encoding='UTF-8')


def dominio(df):
    temp = df['dominio'].value_counts().sort_values(ascending=False)
    exporta(temp, "(c) Dominio")
    

def maiores_dominios(fontes):
    temp = fontes[['municipio', 'populacao_2020','dominio']].sort_values('populacao_2020', ascending=False).head(10)
    exporta(temp, "(c) TOP10-dominios")
    
    
def quantidade_fontes(df):
    um = df[df['qtd_fontes'] == 1].shape[0]
    dois = df[df['qtd_fontes'] == 2].shape[0]
    tres = df[df['qtd_fontes'] == 3].shape[0]
    temp = pd.DataFrame({"Uma fonte": [um], "Duas fontes": [dois], "Três fontes": [tres]}).transpose()
    temp.columns = ["Contagem de cidades"]
    exporta(temp, "(c) quantidade-fontes")
    
    
def tipos_fontes(municipios):
    temp = pd.DataFrame([
    {"tipo_publicacao": "Dedicado ao município", "total": municipios[municipios['fontes_municipio']].shape[0]},
    {"tipo_publicacao": "Associação de municípios", "total": municipios[municipios['fontes_associacao']].shape[0]},
    {"tipo_publicacao": "Publicação do estado", "total": municipios[municipios['fontes_estado']].shape[0]},
    {"tipo_publicacao": "Diário Oficial da União", "total": municipios[municipios['fontes_uniao']].shape[0]},
    {"tipo_publicacao": "Outros", "total": municipios[municipios['fontes_outros']].shape[0]},
    ])
    exporta(temp, "(c) tipos-de-fontes")
    
    
def eh_gov(df):
    govern = df[df["fonte"].str.contains("gov.br", na=False)].shape[0]
    n_govern = df.shape[0] - govern
    temp = pd.DataFrame({"Fonte Governamental": [govern], "Fonte não-Governamental": [n_govern]}).transpose()
    temp.columns = ['Quantidade']
    exporta(temp, "(c) PortaisGOV")
    

def maiores_fontes_gov(fontes):
    temp = fontes[fontes['fonte_governamental']]['dominio'].value_counts().head(10)
    exporta(temp, "(c) TOP10-fontes-governamentais")


def maiores_fontes_privadas(fontes):
    temp = fontes[~fontes['fonte_governamental']]['dominio'].value_counts().head(10)
    exporta(temp, "(c) TOP10-fontes-nao-governamentais")
    

def eh_https(df):
    https = df[df["fonte"].str.contains("https", na=False)].shape[0]
    http = df.shape[0] - https
    temp = pd.DataFrame({"HTTP": [http], "HTTPS": [https]}).transpose()
    temp.columns = ['Quantidade']
    exporta(temp, "(c) HTTPs")





    
    