# Anotações do segundo capitulo do livro engenharia de software do sommerville

## Processos de Software

Os processos de software basicamente são um conjunto coerente de atividades para a produção de um software.
um modelo de processo de software é uma representação simplificada de um processo de software. 
Cada modelo representa uma perspectiva particular de um processo e, portanto, fornece informações parciais sobre ele.

### Quatro atividades fundamentais de processo de software para a engenharia de software

1. _Especificação de software_: A funcionalidade do software e as restrições a seu funcionamento devem ser
definidas.
2. _Projeto e implementação de software_: O software deve ser produzido para atender às especificações.
3. _Validação de software_: O software deve ser validado para garantir que atenda às demandas do cliente.
4. _Evolução de software_: O software deve evoluir para atender às necessidades de mudança dos clientes.

Existem também as atividades que dão apoio ao processo, como _documentação_ e _gerenciamento de configuração de software_.

No entanto, assim como as atividades, as descrições do processo também podem incluir:

1. **Produtos**: que são os resultados de uma das atividades do processo. Por exemplo, o resultado da atividade de pro jeto de arquitetura pode ser um modelo da arquitetura de software.

2. **Papéis**: que refletem as responsabilidades das pessoas envolvidas no processo. Exemplos de papéis são: gerente de projeto, gerente de configuração, programador etc.

3. **Pré e pós-condições**: que são declarações verdadeiras antes e depois de uma atividade do processo ou da produção de um produto. Por exemplo, antes do projeto de arquitetura ser iniciado, pode haver uma pré-condição de que todos os requisitos tenham sido aprovados pelo cliente e, após a conclusão dessa atividade, uma pós-condição poderia ser a de que os modelos UML que descrevem a arquitetura tenham sido revisados.

Vale ressaltar que não existe um processo de software ideal, cada projeto de software pode necessitar de um processo diferente, seja ele mais flexível, mais detalhado e etc.

### As 2 principais classificações dos projetos de software

#### Processos dirigidos

Processos dirigidos a planos são aqueles em que todas as atividades são planejadas com antecedência, e o progresso é avaliado por comparação com o planejamento inicial. 

#### Processos ágeis

Em processos ágeis, que discuto no Capítulo 3, o planejamento é gradativo, e é mais fácil alterar o processo de maneira a refletir as necessidades de mudança dos clientes. 

### Alguns Modelos genéricos de processos de software

_O modelo em cascata_: Esse modelo considera as atividades fundamentais do processo de especificação, desen-
volvimento, validação e evolução, e representa cada uma delas como fases distintas, como: especificação de
requisitos, projeto de software, implementação, teste e assim por diante.

_Desenvolvimento incremental_: Essa abordagem intercala as atividades de especificação, desenvolvimento e va-
lidação. O sistema é desenvolvido como uma série de versões (incrementos), de maneira que cada versão
adiciona funcionalidade à anterior.

_Engenharia de software orientada a reúso_: Essa abordagem é baseada na existência de um número significativo
de componentes reusáveis. O processo de desenvolvimento do sistema concentra-se na integração desses
componentes em um sistema já existente em vez de desenvolver um sistema a partir do zero.

**OBS:** Muitas vezes esses modelos são usados juntos, Principalmente para  desenvolver softwares de grande porte.

### Modelo cascata

Nesse modelo primeiro se planeja as ações antes de devidamente toma-lás é um modelo dirigido a planos básicamente, se só pode chegar na próxima fase do processo após ter concluido a atual.
A conclusão de cada estágio geralmente resulta na aprovação de um ou mais documentos assinados.
E cada estágio desse processo alimenta os outros com informções, pois uma fase gera feedback para outra.
Fazer a manutenção de um software muitas vezes pode significar repetir estágios desse processo.
O modelo cascata é um modelo consistente, pois em cada fase ele gera documentação, tornando assim mais fácil a supervisão do processo e sua organização.
A maior desvantagem desse modelo é a falta de flexibilidade nesses estágios, pois os compromissos e etc devem ser assumidos/designados no inicio do estágio, assim fazendo com que seja mais dificil lidar com mudanças mais repentinas. 
**OBS: esse modelo também é conhecido como modelo de ciclo de vida de um software**

#### Principais estágios do modelo cascata

1. _Análise e definição de requisitos_: Os serviços, restrições e metas do sistema são estabelecidos por meio de consulta aos usuários. Em seguida, são definidos em detalhes e funcionam como uma especificação do
sistema.
2. _Projeto de sistema e software_: O processo de projeto de sistemas aloca os requisitos tanto para sistemas de hardware como para sistemas de software, por meio da definição de uma arquitetura geral do sistema. O projeto
de software envolve identificação e descrição das abstrações fundamentais do sistema de software e seus relacionamentos.
3. _Implementação e teste unitário_: Durante esse estágio, o projeto do software é desenvolvido como um conjunto de programas ou unidades de programa. O teste unitário envolve a verificação de que cada unidade atenda a sua especificação.
4. _Integração e teste de sistema_: As unidades individuais do programa ou programas são integradas e testadas
como um sistema completo para assegurar que os requisitos do software tenham sido atendidos. Após o teste,
o sistema de software é entregue ao cliente.
5. _Operação e manutenção_: Normalmente (embora não necessariamente), essa é a fase mais longa do ciclo de
vida. O sistema é instalado e colocado em uso. A manutenção envolve a correção de erros que não foram
descobertos em estágios iniciais do ciclo de vida, com melhora da implementação das unidades do sistema e
ampliação de seus serviços em resposta às descobertas de novos requisitos.

### Modelo Incremental

A ideia desse modelo é apartir de um modelo inicial que é exposto aos usuários, receber os feedbacks dessas exposições e assim ir fazendo várias versões do software até que ele chegue na versão ideal, a ideia aqui é ir aprimorando o software aos poucos com cada nova exposição.

Fazendo assim uma intercalação entre as atividades de especificação, desenvolvimento e validação, sendo que a cada troca de atividade são dados feedbacks.

O Desenvolvimento incremental é uma parte fundamental das abordagens ágeis, ele funciona muito bem para desenvolvimento de sotwares de negócio, e-commercer e sistemas pessoais.

Ao desenvolver um software de forma incremental, é mais barato e mais fácil fazer mudanças no software durante seu desenvolvimento, pois cada incremento adiciona alguma funcionalidade necessária para o cliente.

O desenvolvimento incremental, atualmente é a mais comum para sistemas aplicativos.

#### Os 2 principais problemas dessa estrutura de processo

1. O processo não é visível. Os gerentes precisam de entregas regulares para mensurar o progresso. Se os sistemas são desenvolvidos com rapidez, não é economicamente viável produzir documentos que reflitam cada uma das versões do sistema.

2. A estrutura do sistema tende a se degradar com a adição dos novos incrementos. A menos que tempo e dinheiro sejam dispendidos em refatoração para melhoria do software, as constantes mudanças tendem a corromper sua estrutura. Incorporar futuras mudanças do software torna-se cada vez mais difícil e oneroso.

Basicamente essa estrutura de processo não funciona muito bem para softwares grandes, pois esses softwares que geralmente são desenvolvidos por equipes separadas, cada uma cuidando de uma parte do software, precisam de processos estáveis, pois assim a organização fica mais clara e menos caótica.

#### 3 Vantagens do desenvolvimento incremental

1. **O custo** de acomodar as mudanças nos _requisitos do cliente é reduzido_. _A quantidade_ de análise e documentação a ser refeita é **muito menor do que o necessário no modelo em cascata**.

2. _É mais fácil obter feedback dos clientes sobre o desenvolvimento que foi feito_. Os clientes podem fazer comentários sobre as demonstrações do software e ver o quanto foi implementado. _Os clientes têm dificuldade_ em avaliar a evolução por meio de documentos de projeto de software.

3. É possível obter **entrega e implementação rápida** de um software útil ao cliente, _mesmo se toda a funcionalidade não for incluída_. Os clientes podem usar e obter ganhos a partir do software inicial antes do que é possível com um processo em cascata.

### Engenharia de software orientada a reúso

Na grande maioria dos projetos ocorre a necessidade de se reutilizar códigos e softwares, no geral isso ocorre de forma informal, pelos devs saberem fontes com códigos semelhantes, assim usando esses códigos após fazerem as mudanças necessárias para serem incorporadas ao sistema.
Esse tipo de reúso ocorre geralmente idependente do processo escolhido, Abordagens orientadas a reúso dependem de uma ampla base de componentes reusáveis de software e de um framework de integração para a composição desses componentes.
Muitas vezes ocorre tambem desses componentes serem sistemas inteiros (COTS) que fornecem uma funcionalidade específica, como processamento de texto.

Embora alguns estágios do modelo de reúso se assemelhem aos estágios de outros modelos, ele tem suas particularidades, sendo os estágios do modelo de reúso os seguintes.

#### Estágios do modelo de reúso

1. _Análise de componentes_: Dada a especificação de requisitos, é feita uma busca por componentes para implementar essa especificação. Em geral, não há correspondência exata, e os componentes que podem ser usados apenas fornecem alguma funcionalidade necessária.

2. _Modificação de requisitos_: Durante esse estágio, os requisitos são analisados usando-se informações sobre os componentes que foram descobertos. Em seguida, estes serão modificados para refletir os componentes disponíveis. No caso de modificações impossíveis, a atividade de análise dos componentes pode ser reinserida na busca por soluções alternativas.

3. _Projeto do sistema com reúso_: Durante esse estágio, o framework do sistema é projetado ou algo existente é reusado. Os projetistas têm em mente os componentes que serão reusados e organizam o framework para reúso.Alguns softwares novos podem ser necessários, se componentes reusáveis não estiverem disponíveis.

4. _Desenvolvimento e integração_: Softwares que não podem ser adquiridos externamente são desenvolvidos, e os componentes e sistemas COTS são integrados para criar o novo sistema. A integração de sistemas, nesse modelo, pode ser parte do processo de desenvolvimento, em vez de uma atividade separada.

#### Os três tipos de componentes de software que podem ser usados em um processo orientado a reúso:

1. Web services desenvolvidos de acordo com os padrões de serviço e que estão disponíveis para invocação remota.
2. Coleções de objetos que são desenvolvidas como um pacote a ser integrado com um framework de componentes, como .NET ou J2EE.
3. Sistemas de software stand-alone configurados para uso em um ambiente particular.

Uma das vantagens desse tipo de modelo é a obvia diminuição na necessidade de código/software a ser feito, além de reduzir os riscos e os custos.
Muitas vezes proporciona também uma entrega mais rápida, mas geralmente os compromisos com os requisitos acabam por se perderem e não entregar realmente o que o cliente precisa, sem contar a falta de controle de uma parte da evolução do software uma vez que esses componentes não estão sobre  jursidição da empresa.