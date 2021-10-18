# -*- coding: utf-8 -*-

def exporta(dados, nome):
    dados.to_csv(path_or_buf="./%s.csv" %(nome), encoding='UTF-8')

     
def diarios_antigos(df):
    df = df[df['data_inicial'] != 'Indefinido']
    top = df.sort_values('data_inicial', ascending=True).filter(items=['municipio', 'regiao', 'populacao_2020','eh_capital','data_inicial']).head(10)
    exporta(top,"TOP10-cidades-antigas")

    
def diarios_novos(df):
    df = df[df['data_inicial'] != 'Indefinido']
    bottom = df.sort_values('data_inicial', ascending=False).filter(items=['municipio', 'regiao', 'populacao_2020','eh_capital','data_inicial']).head(10)
    exporta(bottom,"TOP10-cidades-recentes")


def dist_anual(df):
    df = df['ano_inicial'].value_counts()
    exporta(df,"distribuicao_anual")
