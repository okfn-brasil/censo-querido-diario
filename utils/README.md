# Utilitários do Censo Querido Diário

Este sub-repositório inclui rotinas e funções elaboradas pela comunidade para
processar, analisar e salvar os resultados do Censo Querido Diário.

Atualmente, o único utilitário desenvolvido é o pacote `fetch_portals`, que se
comunica com todos os endereços web cadastrados no Censo para checar quais
portais estão *online* e/ou para obter seu código-fonte.

Contribuições na forma de novos pacotes e utilitários para processar os dados
do Censo são bem-vindas. Cheque o [CONTRIBUTING.md](../CONTRIBUTING.md) do
projeto para mais detalhes de como ajudar nas diferentes tarefas do Censo, bem
como a seção [Adicionando um novo utilitário](#adicionando-um-novo-utilitário)
para instruções específicas de como criar uma nova rotina de pré-processamento.

Se tiver alguma dúvida ou quiser ter uma visão geral dos próximos passos do
Censo, não hesite em visitar as
[issues](https://github.com/okfn-brasil/censo-querido-diario/issues) do projeto
ou entrar em contato pelo [Discord](https://discord.gg/M6ep5VED).

## Instalação e execução

### Com o Docker (recomendado)

A forma mais simples de rodar os utilitários é utilizando o Docker. Você deve
ter instalado o Docker Community Edition. Encontre a versão apropriada para o
seu sistema [aqui][Docker CE]. Você também deve ter o [git] instalado para fazer download do repositório.

Para instalar os utilitários, abra um terminal de linha de comando e rode os
seguintes comandos:

```bash
$ git clone https://github.com/okfn-brasil/censo-querido-diario.git
$ cd censo-querido-diario/utils
```

Em um explorador de arquivos, encontre o diretório onde você fez download do
repositório e abra o arquivo `censo-querido-diario/utils/.env.template`. Adapte
as configurações presentes no arquivo de acordo com os dados que pretende obter
(especialmente as iniciadas em `KAGGLE_*`, se for exportar para o Kaggle).
Salve o arquivo modificado renomeie-o para `.env` (sem o `.template` no final).

Para inicializar a checagem dos portais, basta voltar ao terminal e inserir o
comando:

```bash
$ docker-compose up
```

[Docker CE]: https://hub.docker.com/search?offering=community&type=edition
[git]: https://git-scm.com/

### Como pacote Python

Os utilitários contidos nesse sub-repositório podem ser instalados como pacotes
Python avulsos. Para isso, você deve ter instalada na sua máquina uma versão
Python compatível (3.7 ou superior).

Para instalar a partir do repositório, rode em um terminal de linha de comando:

```bash
$ git clone https://github.com/okfn-brasil/censo-querido-diario.git
$ cd censo-querido-diario/utils
$ python -m venv .venv
$ source .venv/bin/activate  # no PowerShell: $ .venv/Scripts\activate.ps1
(.venv) $ python -m pip install .
```

Para que a instalação funcione e você possa usar o comando `fetch-portals` da
linha de comando, é necessário que antes você exporte algumas variáveis de
ambiente, que controlam o funcionamento do programa.

Para isso, edite o arquivo `.env.template`, contido no diretório
`censo-querido-diario/utils`, alterando as configurações necessárias.
**Importante:** para rodar a versão atual do coletor de portais, você deve, no
mínimo, alterar as variáveis de ambiente iniciadas em `KAGGLE_*`. Você precisa
ter permissão de escrita no dataset utilizado para salvar os resultados.

Quando finalizar a edição, salve o arquivo `.env.template` e renomei-o para
`.env`, apenas.
<!--

No terminal, acesse a pasta `censo-querido-diario/utils` e rode
o seguinte comando:

No Unix/MacOS:

```bash
$ set -a; . .env; set +a
```

No Windows/PowerShell, pode ser necessário adicionar um pacote adicional para
ler as variáveis de ambiente do arquivo `.env` (privilégios de administrador
podem ser necessários):

```powershell
PS> Install-Module -Name Set-PsEnv
```

-->

Com o utilitário instalado como um pacote e o respectivo ambiente virtual
ativado, basta rodar o comando `fetch-portals` na linha de comando. Esse
comando fará requisições a todos os portais de publicação de diários oficiais
mapeados no Censo, e salvará os resultados no dataset do Kaggle indicado no
arquivo `.env`.

```bash
(.venv) $ fetch-portals
```

## Adicionando um novo utilitário

Para desenvolver um pacote Python que consuma e processe os dados do Censo
Querido Diário, [faça um
*fork*](https://github.com/okfn-brasil/censo-querido-diario/fork) do
repositório para a sua própria conta e adicione os scripts em um sub-diretório
da pasta `censo-querido-diario/utils/src`.

Para o nome do diretório e dos módulos, utilize apenas letras minúsculas e
*underscores* (\_). Insira também um arquivo `__init__.py` vazio no diretório
criado, e adicione as dependências utilizadas na lista de pacotes abaixo do
item `install_requires` do arquivo
[`censo-querido-diario/utils/setup.cfg`](./setup.cfg).

Se você quiser que o utilitário seja acessível por meio do Docker, crie um
arquivo chamado `<NOME_DO_UTILITARIO>.Dockerfile` em
`censo-querido-diario/utils`, contendo as instruções de construção do contâiner
(veja a [referência do Dockerfile]). Em seguida, adicione uma entrada no
arquivo `docker-compose.yml` localizado no mesmo diretório (veja a [referência
do Docker Compose] para mais detalhes).

[referência do Dockerfile]: https://docs.docker.com/engine/reference/builder/
[referência do Docker Compose]: https://docs.docker.com/compose/compose-file/
