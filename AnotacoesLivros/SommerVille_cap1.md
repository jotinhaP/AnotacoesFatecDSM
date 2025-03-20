# Anotações do livro Engenharia de software

_Essas anotações são baseadas apenas no capítulo 1_

## Observações
O conceito de engenharia de software foi proposto na _OTAN em 1969_ para a discussão de **resolver problemas ligados ao desenvolvimento de Software**. pois na época existiam muitos problemas relacionados a esse assunto, como por exemplo: Atrasos nos prazos, não entregavam suas devidas funcionalidades e etc.

Mesmo todos os softwares precisando da engenharia de software para serem comstruidos corretamente, difícilmente eles usaram das mesma linhas de pensamento e bases, a engernharia de software tem seus metódos, msa tais metódos variam seu uso com base na _necessidade_ do software, _um jogo de computador não é pensado da mesma forma que um software de geladeira_.

Muitas pessoas definem a engenharia de software como _inadequada para a criação de softwares modernos_.
**SommerVille** em seus livro diz que há duas possíveis razões para tal.

* Aumento da demanda
    Esse fator acaba pesando para a ES pois novas tecnicas de ES nos ajudam a construir softwares mais "sofisticados" as demandas acabam por mudar, se tornando cada vez mais complexas, e tendo a necessidade de entragas rápidas. E devido as tecnicas de engenharia de software atuais não serem suficientes para essas demandas, acabam por passar essa sensação, por isso sommervile afirma ser necessário a criação de novas técnicas para a ES.

* baixas expectativas
    Esse fator acaba por ser de grande peso, pois não é difícil construir um software sem as tecnicas de ES, o que faz com que esses softwares sejam mais caros e menos confiáveis, portanto é necessário ter mais educação quando a ES para que possamos solucionar esses problemas.

## Coisas importantes

Um _Software Profissional_ é aquele que é desenvolvido para um propósito específico de negócio e é usado além daqueles que os desenvolveram.

A Engenharia de software tem por intuito apoiar o desenvolvimento de _software profissional_, incuindo técnicas que apoiam **Especificação, projeto e evolução de programas**.

Quando falamos de engenharia de software _Não estamos nos referindo apenas ao software_ mas também a documentação e os dados de configuração necessários para que ele funcione.

Um software profissional, **muitas vezes é mais que um programa, consistindo muitas vezes de vários programas separados e arquivos de configuração**, que tem como propósito configurar esses programas.

_Documentação do Sistema:_ descreve a estrutura.
_Documentação do Usuário:_ descreve como se usa o programa.

#### Os Dois Principais tipos de Produto de Software:

##### Produtos Genéricos:
São aqueles softwares mais gerais que são vendidos pra qualquer um que os queira usar, como softwares de organização de consultas e etc, esses softwares standAlone não são específicos o suficiente, por isso são considerados genéricos.

##### Produtos sob encomenda:
São aqueles softwares específicos que são encomendados por clientes para cumprir com determinadas funções. Um exemplo disso são programas de controle de tráfego aéreo.

## Dúvidas Comuns que o sommervile responde

**O que é software**: Softwares são programas de computador e _documentação associada_. Produtos de software podem ser _desenvolvidos_ para um **cliente específico ou para o mercado em geral**.

**Quais são os atributos de um bom software**: Um bom software deve prover a _funcionalidade_ e o _desempenho requeridos pelo usuário_; além disso, deve ser _confiável_ e _fácil de manter e usar_.

**O que é engenharia de software**: É uma disciplina de engenharia que se preocupa com **todos** os _aspectos de produção de software_.

**Quais são as principais atividades da engenharia de software**: Especificação de software, desenvolvimento de software, validação de software e evolução de software.

**Qual a diferença entre engenharia de software e ciência da computação**: Ciência da computação foca a teoria e os fundamentos; engenharia de software preocupa-se com o lado prático do desenvolvimento e entrega de softwares úteis.

**Qual a diferença entre engenharia de software e engenharia de sistemas?**: Engenharia de sistemas se preocupa com _todos os aspectos do desenvolvimento de sistemas computacionais_, incluindo _engenharia de hardware_, software e processo. Engenharia de software é uma parte específica desse processo mais genérico (ou seja a engenharia de software se preocupa mais o o software e seus processos).

**Quais são os principais desafios da engenharia de software?**: Lidar com o aumento de diversidade, demandas pela diminuição do tempo para entrega e desenvolvimento de software confiável.

**Melhores técnicas e metodos da engenharia de software**: Enquanto todos os projetos de software devem ser gerenciados e desenvolvidos profissionalmente, técnicas diferentes são adequadas para tipos de sistemas diferentes (ou seja as melhores tecnicas variam de software pra software e necessidade para necessidade).

**Quais diferenças a internet gerou na engenharia de software**: A Internet tornou serviços de software disponíveis e possibilitou o desenvolvimento de sistemas altamente distribuídos baseados em serviços. O desenvolvimento de sistemas baseados em Web gerou importantes avanços nas linguagens de programação e reúso de software.

**Um detalhe importante sobre a diferença de softwares genéricos e sobre encomenda**
Em softwares genéricos, quem o desenvolve que controla suas especificações, já em softwares sob encomenda quem controla e define suas especificações é o cliente.

Uma observação interessante: atualmente a _distinção entre softwares genéricos e sob-encomenda_ está ficando meio _vaga_, pois muitos softwares que podem ser considerados feitos sob-encomenda _usam como base softwares genéricos_, **adaptando-os** para seus _propósitos específicos_.
Sistemas ERP(Sistema integrado de gestão empresarial) são ótimos exemplos desse evento.
Nesse caso, um sistema _grande e complexo é adaptado_ para uma empresa, incorporando _informações_ sobre as **regras e os processos de negócio relatórios necessários** etc.

Falando de qualidade: A qualidade não é _definida apenas pelo que o programa faz_, mas também pelo seu _comportamento_ enquanto ele está _sendo executado_, além de claro incluir a _estrutura_, a _organização dos programas_ e a **documentação do programa**.
E isso acaba por refletir nos atributos de software chamados de **não funcionais** ou **de qualidade**.
Exemplos desses atributos são o _tempo de resposta do software a uma consulta do usuário_ e a _compreensão do código do programa_.

## Caracteristicas essenciais de um sistema profissional de software

**Manutenibilidade**: O software deve ser _escrito_ de forma que possa _evoluir_ para atender às _necessidades dos clientes_. Esse é um **atributo crítico**, porque a mudança de software é um **requisito inevitável** de um ambiente de negócio em mudança.

**Confiança e Proteção**: A confiança do software inclui uma _série de características_ como _confiabilidade, proteção e segurança_. Um software confiável **não deve causar prejuízos físicos ou econômicos** no caso de falha de sistema. _Usuários maliciosos não devem ser capazes de acessar ou prejudicar o sistema_.

**Eficiência**: O software _não deve desperdiçar os recursos do sistema_, como _memória e ciclos do processador_. Portanto, eficiência _inclui capacidade de resposta, tempo de processamento, uso de memória_ etc.

**Aceitabilidade**: O software deve ser aceitável para o tipo de usuário para o qual foi projetado. Isso significa que deve ser compreensível, usável e compatível com outros sistemas usados por ele.

## Se engenharia de software é uma disciplina de engenharia, o que isso quer dizer?

Quer dizer que engenheiros de software focam em todos os aspectos da produção de um software os estágios iniciais da especificação do sistema até sua manutenção, quando o sistema já está sendo usado.
Ou seja assim como engenheiros nós fazemos a coisa funcionar, aplicamos teorias, métodos e ferramentas onde for apropriado, usando essas ferramentas de forma seletiva e tentam descobrir as soluções para os problemas.
E claro tudo isso trabalhando de acordo com as restrições organizacionais e financeiras.

A engenharia de software não se preocupa apenas com os processos técnicos do desenvolvimento de software. Ela também inclui atividades como gerenciamento de projeto de software e desenvolvimento de ferramentas, métodos e teorias para apoiar a produção de software.

## Pontos importantes

* Engenharia de software é uma disciplina de engenharia que se preocupa com todos os aspectos da produção
de software.
* Software não é apenas um programa ou programas; ele inclui também a documentação. Os atributos princi-
pais de um produto de software são manutenibilidade, confiança, proteção, eficiência e aceitabilidade.
* O processo de software inclui todas as atividades envolvidas no desenvolvimento do software. Atividades
de alto nível de especificação, desenvolvimento, validação e evolução são parte de todos os processos de
software.
* As ideias fundamentais da engenharia de software são universalmente aplicáveis para todos os tipos de desen-
volvimento de sistemas. Esses fundamentos incluem processos de software, confiança, proteção, requisitos e
reúso.
* Existem vários tipos diferentes de sistemas, e cada um requer ferramentas e técnicas de engenharia de software
adequadas a seu desenvolvimento. Existem poucas, se houver alguma, técnicas específicas de projeto e imple-
mentação aplicáveis para todos os tipos de sistemas.
* As ideias básicas da engenharia de software são aplicáveis a todos os tipos de sistemas de software. Esses
fundamentos incluem processos de software gerenciados, confiança e proteção de software, engenharia de
requisitos e reúso de software.
* Engenheiros de software têm responsabilidades com a profissão de engenharia e com a sociedade. Eles não
devem se preocupar apenas com as questões técnicas.
* Sociedades profissionais publicam códigos de conduta que definem os padrões de comportamento esperado
de seus membro
