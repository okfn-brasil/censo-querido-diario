# importa bibliotecas
import pandas as pd
from urllib.parse import urlsplit
import nltk
import re

# importa conjunto de dados
municipios = pd.read_csv("./Base_mapeamento_cidades_mais_de_100_mil_habitantes.csv")


def fontes_melted(df):
    fonte_melted = df.melt(value_vars=['fonte_1', 'fonte_2', 'fonte_3', 'fonte_4'], value_name='fonte', ignore_index=False)
    df = df.join(fonte_melted['fonte']).drop(columns=['fonte_1', 'fonte_2', 'fonte_3', 'fonte_4'])
    df = df[df['fonte'] != 'None'].reset_index(drop=True)
    return df

def extrai_path(fontes):
    fontes['fonte_dominio_path'] = fontes['fonte'] \
                .pipe(extract_domain_and_path) \
                .pipe(remove_www) \
                .str.rstrip('/')
    return fontes

def cria_classificacao():
    fontes_associacao = [
    'diariomunicipal.com.br/famep/pesquisar',
    'diariomunicipal.sc.gov.br/site',
    'diariomunicipal.com.br/amupe/pesquisar',
    'diariomunicipal.com.br/amm-mg/pesquisar',
    'diariomunicipal.com.br/amp/pesquisar',
    'diariomunicipal.org/mt/amm/publicacoes',
    'diariomunicipal.com.br/famurs/pesquisar',
    'diariomunicipal.es.gov.br',
    'diariomunicipal.com.br/amupe',
    'diariomunicipal.com.br/aam/pesquisar'
    ]

    fontes_estado = [
    'diariooficial.rs.gov.br',
    'diariooficial.abc.go.gov.br/buscanova',
    'ioepa.com.br/pesquisa',
    'imprensaoficial.com.br/DO/BuscaDO2001Resultado_11_3.aspx',
    'jornalminasgerais.mg.gov.br',
    'pesquisa.doe.seplag.ce.gov.br/doepesquisa/sead.do',
    'ioes.dio.es.gov.br/buscanova',
    'ioerj.com.br/portal/modules/conteudoonline/busca_do.php',
    'diariooficial.ma.gov.br/public/index.xhtml'
    ]

    fontes_uniao = ['in.gov.br/consulta/-/buscar/dou']

    aux = {
    "fontes_associacao": fontes_associacao,
    "fontes_estado": fontes_estado,
    "fontes_uniao":fontes_uniao,
    "fontes_municipio": []
    }

    return aux


def classifica_fontes(fontes, ref_classificacao):
    for classificacao in list(ref_classificacao.keys()):
        fontes[classificacao] = fontes['fonte'].apply(lambda fonte: is_any_of(fonte, ref_classificacao[classificacao]))
    return fontes

def corrige_palavras(fontes):
    fontes['municipio_processado'] = fontes['municipio'] \
        .pipe(remove_uf) \
        .pipe(to_lower) \
        .pipe(only_alphabetic) \
        .pipe(normalize) \
        .pipe(remove_stopwords)
    return fontes

def conflito_em_palavras(fontes):
    fontes['municipio_has_name_word_in_fonte'] = fontes.apply(municipio_has_name_word_in_fonte, axis=1)
    return fontes

def estende_classificacao(ref_classificacao):
    ref_classificacao["fontes_municipio"].extend([
        'portal6.pbh.gov.br/dom/iniciaEdicao.do',
        'dodf.df.gov.br',
        'pmf.sc.gov.br/governo/index.php',
        'pmfi.pr.gov.br/diarioOficial',
        'publicacoesmunicipais.com.br/eatos/hortolandia',
        'domjp.com.br',
        'pjf.mg.gov.br/e_atos/e_atos.php',
        'pjf.mg.gov.br/e_atos/anos_anteriores.php',
        '187.60.128.132:8082/portalcidadao',
        'vozdosmunicipios.com.br/atos.php',
        'pmpf.rs.gov.br/transparencia/secao.php',
        'jornaltribunadonorte.net/editais',
        'diariodesuzano.com.br/noticias/atos-oficiais',
        'cepe.com.br/prefeituradiario',
        'digital.maven.com.br/pub/AtosOficiais',
        'servicos.pmsg.rj.gov.br/diario_oficial.php',
        'servicos2.sjc.sp.gov.br/servicos/portal_da_transparencia/boletim_municipio.aspx',
        'diariooficial.sjp.pr.gov.br/index.php',
        'arquivos.pmspa.rj.gov.br/iframe/boletim-informativo',
        'transparencia.pmspa.rj.gov.br',
        'ts.sp.gov.br/leis-e-normas/imprensa-oficial',
        'dom.pmt.pi.gov.br/lista_diario.php',
        'dom.pmvc.ba.gov.br'
    ])        
    ref_classificacao["fontes_associacao"].extend([
        'diariomunicipal.com.br/ama/pesquisar	',
        'diariomunicipal.com.br/arom/pesquisar',
        'portal6.pbh.gov.br/dom/iniciaEdicao.do',
        'diariomunicipal.com.br/amm-mt/pesquisar',
        'diariomunicipal.com.br/aprece/pesquisar',
        'diariomunicipal.com.br/arom',
        'diariomunicipal.com.br/agm/pesquisar',
        'diariooficialms.com.br/assomasul',
        'diariomunicipal.com.br/ms/pesquisar'
    ])
    ref_classificacao["fontes_estado"].extend([
        'segrase.se.gov.br/buscanova',
        'diario.imprensaoficial.am.gov.br',
        'diario.ac.gov.br',
        'documentos.dioe.pr.gov.br/dioe/consultaPublicaPDF.do',
        'ioes.dio.es.gov.br/caderno_municipios',
        '200.238.101.22/docreader/docmulti.aspx'
    ])
    ref_classificacao["fontes_outros"] = ['tce.mt.gov.br/diario']
    
    return ref_classificacao


def is_any_of(text, words):
    return any([w in text for w in words])

def remove_uf(municipios):
    return municipios.str.replace(' \(\w{2}\)', '')

def to_lower(municipios):
    return municipios.str.lower()

def only_alphabetic(municipios):
    return municipios.str.findall('\w+').str.join(' ')

def normalize(municipios):
    return municipios.str.normalize('NFKD').str.encode('ascii', 'ignore').str.decode('utf8')

def remove_stopwords(municipios):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    stopwords.append('d')  # Necessário para casos como "Santa Barbara D'Oeste"
    return municipios.apply(lambda x: [word for word in x.split() if word not in stopwords]).str.join(' ')

def extract_domain_and_path(df):
    '''(DataFrame) -> DataFrame
    (((explicar o que isso faz)))
    '''
    return df.apply(lambda url: urlsplit(url)[1:3]).str.join('')

def remove_www(df):
    '''(DataFrame) -> DataFrame
    (((explicar o que isso faz)))
    '''
    return df.str.replace('^www\d?\.', '')

def is_any_word_in_text(words, text):
    return bool(re.search('|'.join(words), text))

def municipio_has_name_word_in_fonte(row):
    fonte = re.sub(r'diario|resultado', '', row['fonte_dominio_path'])  # Necessário para casos como Rio Branco (diaRIO) ou Santa Cruz do Sul (reSULtado)
    return is_any_word_in_text(row['municipio_processado'].split(), fonte)
