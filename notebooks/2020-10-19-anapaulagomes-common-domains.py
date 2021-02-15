#!/usr/bin/env python
# coding: utf-8

# # Estatísticas de domínios comuns no censo de Diários Oficiais
# 
# Agora temos uma funcionalidade no site do [Censo](https://censo.ok.org.br/) que permite baixar os dados do mapeamento.
# A partir desses dados, podemos encontrar o domínio base dos diários oficiais e identificar
# potenciais fontes para os _spiders_ do Querido Diário.
# 
# Para reproduzir esse notebook:
# 1. Acesse a página do [andamento do censo](https://censo.ok.org.br/andamento/#view) e faça o download dos dados
# 2. Coloque o arquivo na pasta `notebooks/`

# In[1]:


from urllib.parse import urlparse
import pandas as pd


pd.set_option('display.max_rows', None)
df = pd.read_csv('base_mapeamento.csv', sep=';')


# In[2]:


df.head()


# In[3]:


df = df[df['fonte_1'].notna()]
df['dominio_base'] = df['fonte_1'].apply(lambda url: urlparse(url).netloc)


# ## Domínios com maior população acumulada

# In[4]:


dominios_por_populacao = df.groupby(["dominio_base"])['populacao_2020'].sum()
dominios_por_populacao.reset_index().sort_values(['populacao_2020'], ascending=False).set_index(['dominio_base'])


# ## População por domínios por região

# In[5]:


dominios_por_populacao = df.groupby(["dominio_base", "regiao"])['populacao_2020'].sum()
dominios_por_populacao.reset_index().sort_values(['populacao_2020'], ascending=False).set_index(['regiao'])


# ## População por domínios por estado

# In[6]:


dominios_por_populacao = df.groupby(["dominio_base", "UF"])['populacao_2020'].sum()
dominios_por_populacao.reset_index().sort_values(['populacao_2020'], ascending=False).set_index(['UF'])


# In[7]:


df["dominio_base"].describe()


# ## Número de cidades com o mesmo domínio

# In[9]:


df.value_counts(subset=["dominio_base", "regiao", "UF"], ascending=False)[:10]


# In[ ]:




