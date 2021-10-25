# importa bibliotecas
import pathlib

import pandas as pd

import preprocessamento
import distribuicao_geografica
import formatos_publicacao
import dominios
import acervo_historico

# importa conjunto de dados
municipios = pd.read_csv("./Base_mapeamento_cidades_mais_de_100_mil_habitantes.csv")

# cria diretório onde ficarão os arquivos de saída
pathlib.Path("resultados").mkdir(exist_ok=True)

# PRE-PROCESSAMENTO
municipios = preprocessamento.recorta_perfil(municipios)
municipios = preprocessamento.substitui_sem_diario(municipios)
municipios = preprocessamento.substitui_formato(municipios)
municipios = preprocessamento.remove_variaveis(municipios)
fontes = preprocessamento.trata_fontes(municipios)
municipios = preprocessamento.trata_datas(municipios)
municipios = preprocessamento.conta_fontes(municipios, fontes)


# QUANTIDADES ANALISADAS
n_cidades = municipios.shape[0]
print(f"Mapeamento do relatório: {n_cidades} cidades com mais de 100 mil habitantes mapeadas")
cobertura = n_cidades/5570*100
print(f"Cobertura do relatório: {cobertura}% das cidades do país")
numero_fontes = fontes.shape[0]
print(f"Fontes de publicação de diários oficias mapeadas: {numero_fontes}")


# DISTRIBUIÇÃO GEOGRAFICA
distribuicao_geografica.municipios_por_uf(municipios)
distribuicao_geografica.municipios_por_regiao(municipios)


# FORMATOS DE PUBLICACAO
formatos_publicacao.formatos_publicacao(municipios)
formatos_publicacao.publica_html(municipios)


# FONTES DE PUBLICACAO
dominios.dominio(fontes)
dominios.maiores_dominios(fontes)
dominios.quantidade_fontes(municipios)
dominios.tipos_fontes(fontes)
dominios.eh_gov(fontes)
dominios.maiores_fontes_gov(fontes)
dominios.maiores_fontes_privadas(fontes)
dominios.eh_https(fontes)


# ACERVO HISTÓRICO
acervo_historico.diarios_antigos(municipios)
acervo_historico.diarios_novos(municipios)
acervo_historico.distribuicao_anual(municipios)
