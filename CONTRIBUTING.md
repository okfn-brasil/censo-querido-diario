# Guia de contribuição

Esse documento é um detalhamento sobre como você pode contribuir para o [censo de Diários Oficiais da Open Knowledge Brasil](https://censo.ok.org.br/).
A iniciativa é colaborativa e é liderada pela comunidade de pessoas que seguem a Open Knowledge Brasil nas mídias sociais e pela [Rede de Pessoas Embaixadoras de Inovaço Cívica](https://embaixadoras.ok.org.br/).

Estamos na fase de análise dos dados coletados durante o Censo nos municípios com mais de 100 mil habitantes. Caso você deseje contribuir com essa etapa, incentivamos acessar o post [Faça parte da análise de dados colaborativa do Querido Diário!](https://www.ok.org.br/noticia/faca-parte-da-analise-de-dados-colaborativa-do-querido-diario/) antes de seguir a leitura deste guia .

**Sumário**

[Como interagir com a comunidade?](#como-interagir-com-a-comunidade)

[Para ajudar na coleta de fontes de publicação](#para-ajudar-na-coleta-de-fontes-de-publicação)

[Para ajudar na revisão e validação dos resultados](#para-ajudar-na-revisão-e-validação-dos-resultados)

[Para ajudar na análise e na produção dos relatórios](#para-ajudar-na-análise-e-na-produção-dos-relatórios)

[Ferramentas que utilizamos ou são referências para a produção das análises](#ferramentas-que-utilizamos-ou-são-referências-para-a-produção-das-análises)

## Como interagir com a comunidade?

Entre no nosso discord e acompanhe todas as discussões a respeito do projeto! Link -> https://discord.gg/arxXZXEbGe

## Para ajudar na coleta de fontes de publicação

Nós temos uma força tarefa de coletar as fontes de publicação dos Diários Oficiais municipais, e temos direcionado nossos esforços por recorte populacional, assim conseguiremos fazer as análises de forma pacial até conseguirmos mapear os 5.570 municípios brasileiros.

Escopo | Status
--------- | ------
Capitais | Concluído
Municípios com mais de 100 mil habitantes | Concluído
Municípios com mais de 50 mil habitantes | Em progresso
Municípios com mais de 20 mil habitantes | Em progresso
Todos os 5.570 municípios brasileiros | Em progresso

Acesse o [FAQ da coleta](https://censo.ok.org.br/faq/) e nos ajude a continuar coletando as fontes de publicação de documentos públicos. :)

## Para ajudar na revisão e validação dos resultados

Fizemos um guia exclusivo para ensinar o processo de revisão dos mapeamentos. Lá ensinamos o passo-a-passo de como qualquer pessoa com alguma familiaridade com os sites dos diários pode ajudar a conferir a qualidade dos registros que vão para a base de dados do censo. Veja o guia aqui -> https://hackmd.io/@querido-diario/GUIA-VALIDACAO

## Para ajudar na análise e na produção dos relatórios

Estamos produzindo um [relatório](https://hackmd.io/@querido-diario/report-census-qd-2020-pt) com os resultados do Censo. Para isso, criamos algumas [issues com sugestões](https://github.com/okfn-brasil/censo-querido-diario/issues?q=is%3Aopen+is%3Aissue+label%3Aanalysis) para análise e aceitamos outras sugestões de análises realizadas com os [dados do Censo](https://censo.ok.org.br/andamento/). Não tem problema se a análise proposta não cobre todo o escopo da issue escolhida, também não é necessário que haja visualizações para ilustrá-la. Colabore com o que você puder! A ideia é que as análises e visualizações geradas pelas pessoas contribuidoras façam parte do relatório colaborativo.

Para que isso seja possível, sugerimos realizar todos os passos em um *notebook* público, compartilhando os resultados na [seção de issues](https://github.com/okfn-brasil/censo-querido-diario/issues) do repositório. Você também pode [fazer um fork](https://github.com/okfn-brasil/censo-querido-diario/fork) do repositório, adicionar os notebooks com as análises no diretório `notebooks` e [abrir um *pull request*](https://docs.github.com/pt/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) para incorporar sua sugestão ao repositório do Censo.

Para padronizar o *layout* das visualizações no relatório, usaremos a [ferramenta Flourish](https://app.flourish.studio/). Caso a análise possua alguma representação gráfica, sinta-se livre para usar esta ferramenta ou disponibilizar junto com o notebook a tabela com os dados tratados para cada visualização.

Para quem gosta de escrever, o próprio relatório também está sendo construído a várias mãos. Basta criar uma conta no [HackMD](https://hackmd.io/login) (ferramenta de edição colaborativa de textos que usamos no Censo) e acessar qualquer página do [relatório](https://hackmd.io/@querido-diario/report-census-qd-2020-pt) para ter a opção de editar ou inserir novos trechos.

Se tiver alguma dúvida, faça um comentário na issue relacionada à análise em questão. Ou então nos procure no canal `#censo-querido-diario` do [Discord](https://discord.gg/arxXZXEbGe).

### Ferramentas que utilizamos ou são referências para a produção das análises

- [Ferramenta de escrita e colaboração em markdown - HackMD](https://hackmd.io/@querido-diario)
- [Ferramenta de visualização - Flourish](https://app.flourish.studio/)
- Métricas automatizadas de performance e usabilidade:
  - [Lighthouse](https://github.com/GoogleChrome/lighthouse) 
  - [WebPageTest](https://github.com/WPO-Foundation/webpagetest-docs/)
- Métricas automatizadas de acessibilidade:
  - [Ferramentas recomendadas pela Web Accessibilility Initiative](https://www.w3.org/WAI/test-evaluate/#tools)
  - [Validators, brunopulis](https://github.com/brunopulis/awesome-a11y/blob/master/topics/validators.md)
- [Métricas de complexidade visual e fluência de uso - Interfacemetrics](https://interfacemetrics.aalto.fi/)
- Análise de proprietários de domínios
  - [Whois](https://www.whois.com/)
  - [Registro br](https://registro.br/tecnologia/ferramentas/whois/)
- [Google Search API - para SEO](https://developers.google.com/custom-search/v1/overview)
- [Diretório para os notebooks](https://github.com/okfn-brasil/censo-querido-diario/tree/main/notebooks)
