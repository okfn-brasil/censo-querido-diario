# censo-querido-diario

Temos um longo caminho pela frente. Afinal, precisamos libertar informações de 5.570 municípios. Para começar, queremos fazer um diagnóstico da situação atual dos diários oficiais, reunindo todos os links e os formatos utilizados pelas prefeituras para publicar as informações.

Descubra como colaborar com o mapeamento dos diários oficiais e a análise dos dados deste censo acessando o [Guia de Contribuição](CONTRIBUTING.md).

Se deseja entender mais sobre quais dados são armazenados para que possam ser utilizados posteriormente temos o dicionário de dados [em PDF](data/dicionario-dados-censo-querido-diario.pdf) e [em JSON](data/dicionario-dados-censo-querido-diario.json).

## Dependências do projeto

* [Django](https://www.djangoproject.com/)
* [Git](http://git-scm.com/)
* [Python](https://www.python.org/)
* [Pip](http://www.pip-installer.org/en/latest/)

## Configuração de ambiente


### Criando e ativando ambiente virtual
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### Instalando todas as dependências

```
$ pip install -r requirements.txt
```

### Carregado os dados

Altere o valor da variável `SECRET_KEY` no arquivo `./censo/settings.py` para um valor aleatório.

Gere as migrations e importe os dados.

```
$ python manage.py migrate
$ python manage.py read_data --file data/municipal_data.csv
```

## Executando o projeto
```
$ python manage.py runserver
```
Após subir o Django, verifique na porta 8000:
*http://localhost:8000/*

## Executando relatórios

Na pasta `data` há execuções completas de relatórios publicados a partir dos dados do censo. Se desejar executar um deles, leia arquivo `README.md` do relatório desejado e siga as instruções descritas nele.
