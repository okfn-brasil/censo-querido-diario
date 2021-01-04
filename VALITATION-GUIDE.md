# Guia de validação

Então você já pegou o jeito de [como encontrar um diário oficial](https://censo.ok.org.br/faq/), e está em busca de outras formas de promover a transparência das informações públicas nos municípios?

Ótimo. Você está no lugar certo.

A **validação** é a etapa do mapeamento dos diários oficiais na qual as pessoas voluntárias revisam informações inseridas pelo [formulário](https://censo.ok.org.br/faq/) aberto na página web do Censo QD.

Essa validação é importante porque nem todas as pessoas que contribuem com os mapeamentos têm muita experiência com os conceitos por trás das publicações oficiais (*a ideia é que não precisem ter, mesmo!*). Além disso, há alguns "macetes" e soluções para problemas comuns que só vêm com a prática.

Nessa etapa, as pessoas encarregadas da validação basicamente visitam os portais inseridos como fontes de publicações oficiais e conferem se as informações fornecidas no formulário estão corretas e de acordo com as decisões tomadas pela comunidade do Censo Querido Diário para as questões mais difíceis.

## Ok, entendi. E por onde eu começo?

O primeiro passo para participar da validação é entrar no [servidor da Open Knowledge Brasil no Discord](https://discord.gg/5ysEnvfW). 

É lá - mais especificamente, no canal `#censo-querido-diario` - que acontecem todas as discussões sobre o Censo. Também é por lá que compartilhamos as nossas dúvidas e tentamos resolvê-las coletivamente.

![Canal do Censo Querido Diário no Discord](https://i.imgur.com/otuOHAi.jpg)

Quando você estiver no servidor, dê um '*Olá mundo!*' e avise que você quer contribuir com a validação do Censo. Alguém vai ver e te enviar um par de usuário e senha para acessar a área administrativa  do mapeamento. (**DICA:** *use um `@here` para marcar todo mundo no canal e garantir que todos vão ver a sua mensagem*)

:::info
**Observação**

É possível que, antes de você começar a validar os mapeamentos, alguém te peça para participar de uma das reuniões semanais do Censo. Essas reuniões acontecem sempre às **quintas-feiras, às 19h**, lá no canal de voz **`General`**, no próprio Discord.
:::

Com as suas credenciais, acesse o site [`https://censo.ok.org.br/admin/`](https://censo.ok.org.br/admin/) e faça login para a área de administração do Censo.

![Login no painel de administração do Censo](https://i.imgur.com/eTbCBFP.png)


## O painel de administração

### Visão geral

A primeira visão que você terá ao entrar no painel de administração será algo assim:

![Visão geral do painel de administração, com números indicando os principas menus](https://i.imgur.com/ZcrThdW.png)

Os números da imagem mostram as principais áreas do painel:

1. **Visões dos formulários**. É aqui que estão guardados os formulários submetidos pelo site do Censo QD, divididos por recortes de população e por status - mapeado (*mas ainda não validado*) ou mapeado **E** validado.
2. **Suas ações recentes**. Quando você começar a editar os mapeamentos, seus últimos envios aparecerão aqui. Caso você perceba que cometeu algum erro e precise voltar em um mapeamento já enviado, esse é o lugar mais fácil de encontrá-lo.
3. **Botão de sair**. Para sair do painel 🙃

Na primeira etapa do censo, a prioridade são as cidades **acima de 100 mil habitantes**. Para ver os mapeamentos pendentes de validação para essa faixa, basta clicar no link do formulário `Mapeamento cem mil habitantes`.

### Visão dos municípios pendentes

A página seguinte será semelhante à anterior, mas conterá, na parte central, uma lista de municípios cujo mapeamento ainda está pendente de revisão.

![Lista de municípios com mapeamento pendente](https://i.imgur.com/evf1LIO.png)

Para começar a revisar os mapeamentos, basta escolher um município da lista com o qual você simpatizar mais. Clique no nome dele para abrir o formulário.

### O formulário

![Formulário de mapeamento de publicações oficiais, visto no painel de administração](https://i.imgur.com/fjN2ZoI.png)

Há quatro conjuntos principais de campos no formulário:

1. **Fontes**. Cada fonte é um endereço da web onde são publicados os atos oficiais do município. Cada município pode ter até quatro fontes associadas.
2. **Informações básicas sobre as publicações**. Essas informações incluem se as publicações são disponibilizadas online, desde quando e em qual formato.
3. **Caixa de seleção `☑ Validação`**. Se marcada, indica que o mapeamento foi revisado e está pronto para ser incorporado à base de dados final do Censo.
4. **Campos `Observações` e `Anomalia obs`**. São campos visíveis apenas no ambiente de administração e servem para acrescentar outros detalhes importantes sobre as publicações (*mais detalhes abaixo*).

Ao final do formulário, há um botão **`Save`**, que guarda as alterações realizadas. Esse botão **NÃO** envia necessariamente as informações para a base definitiva do Censo. Para isso, é preciso selecionar a caixa `☑ Validação`, e só então salvar.

A seção a seguir detalha os procedimentos para revisar as informações de cada um desses campos.

:::warning
**ATENÇÃO**

O campo **`navegacao`** está no formulário por razões históricas. Apenas deixe-o como está, em branco.
:::

## Revisando um mapeamento

### Fontes

![Exemplo de seção "Fontes", para o município de Sapucaia do Sul (RS)](https://i.imgur.com/YJK5zRl.png)


Cada fonte de publicação é um endereço disponível online onde podem ser encontrados os atos oficiais da Prefeitura do município, agrupados por data de publicação (*ver quadro abaixo*).

Para cada fonte registrada, a pessoa que está validando o formulário deve:

- Copiar o link em uma nova aba em seu navegador e verificar se a fonte registrada está realmente disponível online;
- Verificar se a fonte registrada é realmente um portal de publicações oficiais (*ver a distinção [abaixo](#Site-da-Prefeitura-ou-portal-da-transpar%C3%AAncia-como-fontes-de-publica%C3%A7%C3%A3o) entre portal de publicações oficiais e portal da transparência e outros sites*).
- Verificar se o portal publica atos do município para o qual ele foi mapeado, e se essas publicações são do Poder Executivo municipal (prefeitura) - e não da Câmara de Vereadores, por exemplo.
- No caso de portais com mais de um município, verificar se a URL registrada encaminha diretamente para a visão dos atos do município registrado. Se for possível gerar um link compartilhável que filtre apenas as publicações do município mapeado, esse link deve ser preferido (*ver quadro a seguir*).

:::info
**Observação**

Gerar uma URL para filtrar um município em um portal com atos oficiais de diferentes entes públicos pode exigir um pouco de experimentação e criatividade.

Muitas vezes, é necessário aplicar os filtros de busca manualmente e verificar na URL gerada quais "pedaços" são necessários para reproduzir a busca. Geralmente, esses pedaços vêm na parte final da URL, depois de um caractere `?` e separados por caracteres `&`.

Por exemplo, em uma busca no portal hipotético `https://diariobacana.org.br/busca?municipio=Cidadopolis&data-inicial=2020-01-01&data-final=2020-12-31`, colar apenas a parte `https://diariobacana.org.br/busca?municipio=Cidadopolis` pode ser suficiente para reproduzir a busca por um município. Se estiver na dúvida, você pode colar o link em uma janela anônima do seu navegador e ver o que aparece.

Gerar essas URLs é uma habilidade relativamente avançada e **não é obrigatória** para validar o mapeamento. Às vezes, sequer é possível gerar uma URL que reproduza a busca. Nesses casos, ou se ficar em dúvida, **valide o município apenas com a base da URL** - aquela que é suficiente para você abrir a página e fazer a busca.
:::

Se todos esses aspectos parecerem corretos, você pode considerar legítima a fonte de publicação registrada. Na maioria dos casos, haverá apenas uma fonte de publicação para o município. Se houver mais de uma, veja a seção "[Municípios com várias fontes de publicação](#Munic%C3%ADpios-com-v%C3%A1rias-fontes-de-publica%C3%A7%C3%A3o)" para conferir como essas fontes devem ser ordenadas.

### Informações básicas

#### Está online

![Exemplo de campo "Is online"](https://i.imgur.com/udGZvXd.png)

Se você já verificou as fontes de publicação acima e havia pelo menos uma fonte de publicação legítima e atual (com atos recentes), é porque há um portal de diários oficiais online para aquele município. Basta garantir que a opção **`Sim`** está selecionada no campo **`Is online`** e seguir em frente.

Registros que estiverem sem fonte de publicação, ou que estiverem com a opção `Sem confirmação` selecionada devem ter um tratamento diferente e **não devem ser validados**. Veja a seção "[Município registrado como `Sem confirmação` ou como `Não` tem publicação online](#Munic%C3%ADpio-registrado-como-Sem-confirma%C3%A7%C3%A3o-ou-como-N%C3%A3o-tem-publica%C3%A7%C3%A3o-online)" sobre como lidar com esses casos.

#### Data inicial

![Exemplo de campo "Data inicial", com a data de 9 de novembro de 2017 selecionada](https://i.imgur.com/vBG1fE9.png)

A data inicial presente nesse campo deve ser a primeira data a partir da qual há a publicação **regular** (*semanal, diária etc.*) de atos oficiais nos portais elencados na seção `Fontes`. Se houver mais de um portal, a data inicial deve incluir as publicações em todos os portais.

Na maioria das vezes, para validar esse dado, basta navegar nos portais. A maioria deles possui algum tipo de paginação, com os atos ordenados do mais recente para o mais antigo. Assim, basta ir até a última página para descobrir quando ocorreram as primeiras publicações.

Em alguns casos, pode ser necessário realizar uma consulta por intervalo de datas para encontrar as publicações. Nesses casos, insira uma data inicial suficientemente antiga (por exemplo `01/01/1900`, ou a primeira que for permitida). Em seguida, busque os registros mais antigos retornados.

Na seção "[Não consigo ver qual foi o dia inicial da publicação](#N%C3%A3o-consigo-ver-qual-foi-o-dia-inicial-da-publica%C3%A7%C3%A3o)" há algumas dicas para casos mais difíceis, quando essas técnicas não funcionarem.

#### Formato do arquivo

![Exemplo de campo "Tipo do arquivo", com a opção "HTML" selecionada](https://i.imgur.com/ZFMhmSW.png)

O campo **`Tipo arquivo`** se refere ao formato em que o texto das publicações estão disponíveis para consulta e download. São seis as opções:

1. **PDF texto**. Arquivos PDF baixados ou visualizados no navegador, que tenham seus conteúdos selecionáveis e copiáveis como textos.
2. **PDF imagem**. Arquivos PDF em que os conteúdos aparecem como imagens (geralmente, documentos escaneados), ou seja, não podem ser selecionados e copiados com o cursor.
3. **DOCX**. Formato de documento do Microsoft Word, versão 2007 em diante.
4. **TXT**. Formato de texto simples, como o utilizado por editores como o Bloco de Notas (*Windows*), o TextEdit (*MacOS*) e o Gedit, Leafpad ou KWrite (*Unix*).
5. **HTML**. É o formato de documento utilizado nos navegadores web. Em geral, as publicações estão em HTML quando os atos *inteiros* podem ser visualizados dentro do portal ou como uma janela à parte, com o conteúdo selecionável como se fosse um texto qualquer de uma página web.
6. **Outros formatos**. As publicações estão disponíveis apenas em outro(s) formato(s) não listado(s) acima.

:::info
**Observação:**

As categorias PDF-Texto e PDF-Imagem podem gerar dúvidas à primeira vista. Se estiver na dúvida sobre qual delas é a mais precisa para uma publicação, baixe o arquivo, abra-o em um programa visualizador de PDFs e tente selecionar um trecho de texto. Se o trecho for selecionado normalmente, o arquivo é PDF-Texto.

Às vezes, uma publicação pode ter tanto trechos de texto, quanto partes escaneadas e reproduzidas como imagem. Nesse caso use o bom senso, mas privilegie a classificação como **PDF-Imagem** se as partes nessa condição forem significativas (*algo como 40% dos atos, ou mais*).
:::

A validação desse campo implica acessar e/ou baixar uma edição recente da publicação oficial e verificar em qual formato ela é disponibilizada. Se houver mais de um formato disponível, consulte a seção "[Diferentes formatos de arquivo para a mesma publicação](#Diferentes-formatos-de-arquivo-para-a-mesma-publica%C3%A7%C3%A3o)" para verificar qual formato deve ser preferido no registro.

### Informações adicionais (`Observações` e `Anomalias`)

Os campos `Observações` e `Anomalias` foram criados para registrar informações adicionais consideradas importantes pelas pessoas responsáveis pela validação.

Esses campos não são visíveis na versão pública do formulário. Eles devem ser preenchidos apenas se você sentir necessidade de registrar uma observação sobre os campos validados (campo `Observações`), ou se notar alguma barreira ao acesso às publicações não prevista no formulário.

#### Observações

![Exemplo de campo "Observações" para o município de Vitória (ES)](https://i.imgur.com/RMu8C1H.png)

O campo `Observações` permite à pessoa que está realizando a validação justificar as suas decisões e incorporar informações adicionais sobre como interpretar os campos do mapeamento.

Esse campo é especialmente útil quando é necessário diferenciar dados para diferentes portais de publicação em um município. Embora a regra seja privilegiar sempre o mais recente - exceto para a data inicial, que deve considerar todas as fontes -, pode ser interessante registrar as datas em que o município começou a publicar em cada fonte e os respectivos formatos de publicação, por exemplo.

Também é aqui que deve ficar registrado se forem encontradas apenas fontes de publicação com os atos "avulsos" (*veja mais na seção "[Site da Prefeitura ou portal da transparência como fontes de publicação](#Site-da-Prefeitura-ou-portal-da-transpar%C3%AAncia-como-fontes-de-publica%C3%A7%C3%A3o)", abaixo*).

#### Anomalias

![Exemplo de campo "Anomalias" para o município de Guarulhos (SP)](https://i.imgur.com/NW2fuEk.png)

O campo `Anomalias` se destina a qualquer tipo de restrição ou barreira ao acesso às publicações percebida pela pessoa que está fazendo a validação. Vale desde dificuldades com os campos de busca até instabilidades no site ou períodos sem publicação de atos oficiais, entre outros.

Uma anomalia especialmente comum, que merece ser registrada sempre que aparece, é a presença de testes do tipo CAPTCHA. Além de dificultar o acesso automatizado a informações públicas, esses dispositivos impedem o uso dos portais por pessoas que precisam de tecnologias asssistivas, como leitores de tela.

![Exemplo de portal de publicações oficias com CAPTCHA](https://i.imgur.com/pUaruPQ.jpg)

## Dúvidas e problemas comuns

### Site da Prefeitura ou portal da transparência como fontes de publicação

Por vezes, são mapeados como portais de publicações oficiais outros sites das prefeituras, onde alguns atos oficiais são reproduzidos. Geralmente, esses atos aparecem "avulsos" - ou seja, não estão divididos em edições diárias ou semanais, acessíveis em um único arquivo ou diretório.

O caso mais comum é que sejam apontados os Portais da Transparência, já que [é obrigatório](http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm#art8) que lá estejam linkados ou reproduzidos alguns atos específicos.

No entendimento atual do Censo QD, esses portais **não devem ser considerados como fontes de publicações oficiais**. 

Para ser considerada uma fonte de publicação, o portal deve conter um mínimo de estrutura para as publicações - em edições diárias, semanais ou suplementares. Ainda mais importante, a fonte não deve conter apenas um ou poucos tipos de ato  - por exemplo, disponibilizar apenas editais de licitação ou avisos de concursos públicos, mas não atos de nomeação e exoneração de servidores, que são bastante comuns.

Se um mapeamento que você estiver validando contiver apenas esse tipo de fonte, considere como se nenhuma fonte tivesse sido registrada. Nesse caso, proceda da mesma forma que está descrita na seção "[Município registrado como Sem confirmação ou como Não tem publicação online](#Munic%C3%ADpio-registrado-como-Sem-confirma%C3%A7%C3%A3o-ou-como-N%C3%A3o-tem-publica%C3%A7%C3%A3o-online)".

### Municípios com várias fontes de publicação

Por vezes, são registradas várias fontes de publicação para um mesmo município. 

Isso costuma acontecer porque o município publica seus atos em mais de um veículo (no diário de uma associação de municípios e imprensa oficial do seu estado, por exemplo), ou porque trocou uma ou mais vezes de portal.

Nesses casos, todos os portais que tenham publicações oficiais referentes ao município devem estar cadastradas como fontes. Algumas regras devem ser seguidas para a ordem em que as fontes são registradas no formulário:

- A fonte principal (*Fonte 1*) em uso atualmente para a publicação de atos oficiais.
- Se houver uma sequência temporal clara nos períodos de publicação de cada fonte, as fontes secundárias também devem ser ordenadas da mais recente para a menos recente.
- Se houver mais de uma fonte atual ou para o mesmo período, deve ser dada a preferência para os portais "oficiais" da prefeitura (endereços com `.gov.br`), em oposição a portais de notícias locais ou de associações de municípios.

A fonte principal (*Fonte 1*) é a que deve ser considerada para preencher as informações básicas de formato do arquivo. Para a data inicial, deve ser considerada a primeira data em que as publicações começam a ser realizadas com regularidade em qualquer uma das fontes.

### Diferentes formatos de arquivo para a mesma publicação

Não é incomum que os portais de publicações oficiais disponibilizem mais de um formato para visualização e/ou download das edições e dos atos.

Nesse caso, a regra geral é registrar o formato "mais aberto" disponibilizado. A tabela a seguir mostra essa ordem, do mais preferido para o menos:



|      Formato     | Observação |
| ---------------- | ---------- |
| **Outros formatos**  | Se for um formato (semi)estruturado: XML, JSON etc.     |
| **TXT** | Arquivo de texto sem formatação |
| **HTML** | Formato web comum |
| **DOCX** | Arquivo do Microsoft Word 2007+ |
| **PDF*** | Arquivo PDF (texto ou imagem) |

\* Os arquivos PDF devem ser registrados como PDF-Imagem se contarem com trechos significativos (40% ou mais) de documentos escaneados, ou como PDF-Texto caso predominem textos selecionáveis.

Adicionar uma nota sobre os diferentes tipos de formatos disponíveis nas `Observações` é opcional, mas recomendado caso os diferentes formatos ocorram em portais diferentes.

### Não consigo ver qual foi o dia inicial da publicação

Alguns portais restringem a consulta por datas a um intervalo de seis meses - ou, pior, sequer disponibilizam uma consulta por datas.

Algumas dicas podem ajudar a encontrar a data inicial nesses casos:

#### Portais sem consulta por data

Se o portal não apresenta todo o histórico imediatamente e possui apenas uma busca por termos, sem busca por datas, você pode forçá-lo a mostrar todos os resultados buscando um termo muito comum. 

Uma escolha certeira é realizar uma busca apenas pela letra `a`. Como todas as edições devem conter essa letra, o resultado deve conter todo o histórico das publicações oficiais - basta ordená-las por data e buscar a primeira.

#### Truque para diários no SIGPUB (domínio `diariomunicipal.com.br/...`)

O SIGPUB é uma solução muito comum para divulgação de atos oficiais por associações de municípios. Entre outras barreiras de acesso, esse sistema restringe a busca de atos oficiais a intervalos de seis meses.

![Exemplo de portal de buscas com o sistema SIGPUB](https://i.imgur.com/uT9zvux.png)

Felizmente, há uma forma de contornar essa restrição. Basta seguir os passos seguintes:

1. Acesse a página de busca de atos da associação desejada (a URL se parecerá com `http://www.diariomunicipal.com.br/<SIGLA-DA-ASSOCIAÇÃO>/pesquisar`).
2. Selecione o nome do município desejado no campo `Município (Entidade)`. *Deixe os demais campos inalterados.*
3. Clique no botão `Pesquisar`. Resolva o reCAPTCHA, se for solicitado.
4. Ignore o resultado que apareceu. Ainda na mesma página, no formulário de busca, altere o valor no campo `Data Início da Circulação` para `01/01/1900`. Clique em `Pesquisar` novamente e responda o reCAPTCHA se for solicitado.
5. Navegue até a última página dos resultados retornados. Registre a data do primeiro ato como data inicial no formulário.

#### Regra geral para outros casos

Nos demais casos, pode ser necessário usar uma estratégia de "cercar" a data de publicação inicial. 

Para isso, defina um intervalo com o período máximo aceito pelo site - por exemplo, 01/01/2019 a 30/06/2019. Realize a busca e verifique se há resultados desde o início do período.

Em seguida, repita a mesma busca, mudando apenas o ano para um pouco antes - por exemplo, 01/01/2017 a 30/06/2017. Verifique se ainda há resultados cobrindo todo o período.

Repita o procedimento até deixar de ver resultados, ou que eles cubram apenas alguns meses do período. Se isso estiver demorando a acontecer, aumente o intervalo de anos entre as buscas - alguns (poucos) diários têm acervos de décadas.

Uma vez que deixem de aparecer resultados, "avance" de volta alguns anos ou meses em direção ao último intervalo para o qual verificou que havia resultados. Repita isso até encontrar a data de início das publicações - ela deve estar em algum lugar entre os dois intervalos.

:::info
**Observação**

Se você sente segurança em manipular buscas diretamente por meio da URL, você pode fazer isso para alterar os intervalos de datas. Isso pode tornar as buscas um pouco mais ágeis.
:::

### Município registrado como `Sem confirmação` ou como `Não` tem publicação online

O formulário aberto do Censo QD permite que um município seja cadastrado como `Sem confirmação` ou como `Não` tem publicação online. A diferença entre ambos é que, no segundo caso, espera-se que a pessoa que realizou o mapeamento tenha entrado em contato com a prefeitura para comprovar a ausência de fonte de publicação online.

O problema é que, muitas vezes, é difícil comprovar se esse contato foi realizado devidamente e se a busca foi feita de forma cuidadosa. Comprovar a *falta* de algo  é bem mais difícil do que comprovar a eixstência dela.

A orientação para pessoas novatas na validação é **deletar** esses registros, forçando a cidade a voltar à lista de municípios pendentes de mapeamento no formulário público.

Na prática, porém, muitas pessoas preferem realizar logo uma busca mais aprofundada para tentar encontrar uma fonte de publicação. Muitas vezes, funciona.

Algumas dicas que podem ajudar - e que vão além do tradicional procurar em um mecanismo de busca `"Diário Oficial <NOME DO MUNICÍPIO>"`:

- Busque na imprensa oficial do estado a qual pertence o município. Muitos municípios publicam em um caderno ou seção específicos do diário oficial do seu estado.
- Busque se há alguma associação de municípios que publique os atos oficiais dos seus associados naquele estado. Muitas dessas associações são acessíveis pelo portal `www.diariomunicipal.com.br`.
- No site da prefeitura, verifique se há uma barra de buscas e procure por `"Diário Oficial"` (com aspas). Muitas vezes, há alguma notícia que pelo menos dê indicação de onde são publicados os atos oficiais.
- Procure em sites de concursos públicos pelo nome do município. Esses sites costumam reproduzir os editais e indicar onde foram publicados os originais.

Se nada disso funcionar, registre os principais passos tomados no campo `Observações`. Se puder, procure o telefone da prefeitura e tente entrar em contato. Diga que está fazendo uma pesquisa e gostaria de saber onde são publicados editais e avisos oficiais da prefeitura.

Se a prefeitura confirmar que não há fonte de publicação online, é seguro apontar o campo `Is online` como `Não`. Esses casos não são comuns, mas podem ocorrer em locais onde as publicações da prefeitura são feitas em jornais locais, sem versão digital.

### Posso validar um município que eu mapeei?

Idealmente, não.

Essa situação pode acontecer com quem contribui tanto com o mapeamento, quanto com a validação. Nesses casos, pode ser tentador mapear e, logo em seguida, validar os municípios - só pela emoção de ver o contador de cidades registradas crescer.

Apesar disso, o ideal é manter as duas funções separadas. Afinal, a ideia por trás da validação é justamente ter um segundo olhar para garantir que haja conformidade com os princípios adotados no projeto. Quanto mais olhos, menor a chance de erros.

## Na dúvida, pergunte!

Esperamos que esse guia cubra as principais situações de dúvidas que surgiram até agora no processo de mapeamento e validação.

Porém, nesse mundo, sempre haverá algum caso imprevisto ou que gere dúvidas de como interpretar os princípios que estão neste Guia.

**Se estiver na dúvida, não sofra, nem arrisque**. O [canal do Discord](https://discord.gg/5ysEnvfW) está sempre aberto para acolher qualquer tipo de dúvida - das mais simples às mais complexas. Por vezes, podem aparecer questões novas. O debate em grupo ajuda a tomar uma posição comum e garantir que ela se estenda aos próximos mapeamentos.

---

**Referência rápida:**

[TOC]

---

###### tags: `Census` `Guidelines` `pt`