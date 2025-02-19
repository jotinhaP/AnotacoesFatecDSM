# Anotações da Aula de Modalagem de Banco de Dados I

O que são dados?
São fragmentos de informação, portanto não tem sentido lógico conclusivo.

informação é um conjunto organizado de dados.

As informações geral reações diferentes me usuários, por isso temos que garantir que os dados sejam organizados de forma que o usuário consiga entender com facilidade seu significado.

A importancia da modelagem é fazer um banco que seja rápido, otimizavel.

Tudo que precisa ser feito tem que ser consultado e armazenado no banco geralmente.

O banco de dados precisa estar sistematicamente organizado para que os dados sejam fáceis de se encontrar.

O tipo de dado _data_ é sempre muito complexo pois cada lugar pode ter sua forma de formatação, o que faz com que a sintax varie.

data -> informação -> conhecimento.

Abstração = a forma que cada um entende sobre algo.

As 4 etapas para se montar um banco

_Análise de requisitos_ é a parte que busca os dados e seus tipos que se precisa estar no banco, seja se conversando com o usário e etc.

_Modelo Conceitual_ é mais abstrato, onde nós vemos mais ou menos estrutura que o banco deverá ter e o que queremos usar (**essa parte não é muito usada comercialmente**).

_Modelo Lógico_ é a parte que começamos a ver com mais detalhes o que precisaremos usar e como vamos fazer.

_Modelo Físico_ Aqui vamos pegar todos os modelos e planos anteriores e vamos programar o banco.

## Trechos tirados da apostila Cáp 1 - **Conceitos**.

Um banco de dados é uma coleção de _dados relacionados_. Com dados, queremos 
dizer fatos conhecidos que podem ser registrados e possuem significado implícito.

_O que são dados???_

Dados são _observações documentadas ou resultados da medição_. A disponibilidade dos 
dados oferece oportunidades para a obtenção de informações.

**Diferença de DADO e INFORMAÇÃO**

_Dado =_ O dado não possui significado relevante e não conduz a nenhuma compreensão. 
Representa algo que não tem sentido a princípio. Portanto, não tem valor algum para 
embasar conclusões, muito menos respaldar decisões.

_Informação =_ A informação é a ordenação e organização dos dados de forma a transmitir significado 
e compreensão dentro de um determinado contexto. Seria o conjunto ou consolidação dos dados de forma a fundamentar o conhecimento.

## Cápitulo 2 da Apostila 1 -- Modelo Conceitual

### Fazendo um Modelo Conceitual 

**O que é uma Entidade?**

Uma entidade _é um objeto ou ente do mundo real_ que possui existência própria e **cujas características ou propriedades desejamos registrar**. Ela pode ter uma existência física ou abstrata. 
_Exemplo_: Em uma faculdade teríamos Alunos, Professores, Disciplinas ou Cursos
Nos modelos Conceituais as entidades são representadas por retangulos.

**Atributos das Entidades**

Uma entidade é caracterizada por algumas propriedades específicas que achamos 
importante registrar e que são denominados atributos.
_Exemplo_: RG, CPF, NOME.

Os atributos são representados no modelo conceitual por meio de elipses, ligadas a Entidade.

**Relacionamentos**

O relacionamento no banco de dados _é a forma com as Entidades se associam_. Os 
relacionamentos apenas podem associar **ENTIDADES**. 
Os relacionamentos são representados por losangos, com uma descrição da associação.

**Cardinalidade**

É o _número máximo e mínimo de ocorrências/Registros_ de uma entidade que estão associadas às 
ocorrências/Registros de _outra entidade que participa do relacionamento_.
A Cardinalidade é importante para definir o relacionamento, pois ela define o numero de ocorrencias/registros de um relacionamento(__isso aqui é basicamente o um pra vários, o vários pra um e o cara***__).