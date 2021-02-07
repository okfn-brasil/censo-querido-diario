# censo-querido-diario

Temos um longo caminho pela frente. Afinal, precisamos libertar informações de 5.570 municípios. Para começar, queremos fazer um diagnóstico da situação atual dos diários oficiais, reunindo todos os links e os formatos utilizados pelas prefeituras para publicar as informações.

## Requirements

* [Django](https://www.djangoproject.com/)
* [Git](http://git-scm.com/)
* [Python](https://www.python.org/)
* [Pip](http://www.pip-installer.org/en/latest/)
* [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

## Configuração de ambiente para rodar local

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

## Configuração de ambiente para rodar via Docker

Basta ter o [Docker instalado](https://docs.docker.com/get-docker/) e rodar o seguinte comando:

```shell
$ docker-compose up --build -d
```

Acesse via:
*http://localhost:8000/*

Se precisar olhe o log através do seguinte comando:
```shell
$ docker logs censo [-f]
```
