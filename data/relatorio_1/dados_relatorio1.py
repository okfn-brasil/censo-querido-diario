#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# importa bibliotecas
import pandas as pd

import preprocessamento as prep
import distribuicao_geografica as dg
import formatos_publicacao as fp
import dominios as dm
import acervo_historico as ah


def exporta(dados, nome):
    dados.to_csv(path_or_buf="./%s.csv" %(nome), encoding='UTF-8')


# importa conjunto de dados
df = pd.read_csv("./Base_mapeamento_cidades_mais_de_100_mil_habitantes.csv")

# PRE-PROCESSAMENTO
df = prep.recorta_perfil(df)
df = prep.substitui_sem_diario(df)
df = prep.substitui_formato(df)
df = prep.remove_variaveis(df)
fontes = prep.trata_fontes(df)
df = prep.trata_datas(df)
df = prep.conta_fontes(df, fontes)

'''
# REMOVER: INICIO

print("Vasculhando dados estranhos")
variaveis = df.columns
for variavel in variaveis:
    conjunto = df[variavel].value_counts().sort_values()
    print(variavel, '\n', conjunto)
    print("universo:", conjunto.sum())
    print('\n'*5)
    exporta(conjunto, variavel)

# REMOVER: FIM     
'''
# QUANTIDADES ANALISADAS
n_cidades = df.shape[0]
print("Mapeamento: %.f cidades mapeadas" %(n_cidades))
cobertura = n_cidades/5570*100
print("Cobertura: %.2f porcento das cidades do país" %(cobertura))
n_fontes = fontes.shape[0]
print("Fontes: %.f" %(n_fontes))

'''
# DISTRIBUIÇÃO GEOGRAFICA
dg.municipios_UF(df)
dg.municipios_regiao(df)

# FORMATOS DE PUBLICACAO 
# municipios
fp.formatos_publicacao(df)          # estatisticas do formato
fp.publica_HTML(df)                     # destaque às publicacoes em HTML
fp.formatos_capitais(df)                # recorte para as capitais
# UF
fp.formatos_UF(df)                  # estatisticas do formato



# FONTES DE PUBLICACAO
dm.dominio(fontes)
dm.dominio_maior_um(fontes)
dm.dominio_UF(fontes)
dm.publica_HTML(fontes)
####### dm.pub_agrupamentos(fontes)
dm.is_gov(fontes)
dm.is_https(fontes)
dm.qntd_fontes(df)
dm.qntd_fontes_capital(df)
'''

# ACERVO HISTÓRICO
ah.diarios_antigos(df)
ah.diarios_novos(df)
ah.dist_anual(df)
ah.lista_anos(df)
