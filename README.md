# censo-querido-diario

Temos um longo caminho pela frente. Afinal, precisamos libertar informações de 5.570 municípios. Para começar, queremos fazer um diagnóstico da situação atual dos diários oficiais, reunindo todos os links e os formatos utilizados pelas prefeituras para publicar as informações. 

Descubra como colaborar com o mapeamento dos diários oficiais e a análise dos dados deste censo acessando o [Guia de Contribuição](CONTRIBUTING.md).

## Requirements

* [Django](https://www.djangoproject.com/)
* [Git](http://git-scm.com/)
* [Python](https://www.python.org/)
* [Pip](http://www.pip-installer.org/en/latest/)
* [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

## Configuração de Ambiente

### **Instalando todas as dependências**

```
$ mkvirtualenv censo -p python3
$ pip install -r requirements.txt
```

### Carregado os dados
```
$ python manage.py migrate
$ python manage.py read_data --file data/municipal_data.csv
```

## Executando o Projeto
```
$ python manage.py runserver
```
Após subir o Django, verifique na porta 8000:
*http://localhost:8000/*
