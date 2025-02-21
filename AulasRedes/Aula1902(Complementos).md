# Aqui estão alguns complementos para a aula térrivel do Ismael do dia 19/02

## **THREADS** o que são? para que servem? e etc

#### Definição

Thread (linha de execução) é uma **sequência de instruções** que faz parte de um processo principal.
Básicamente _um software é divido em processos_ e os processos _divididos em threads_, e essas threads formam tarefas indepentes mas que se relacionam entre si.

#### Como funciona?

Primeiro o _S.O_ oraganiza as _tarefas que devem ser executadas_ em processos, e essas são dividas em _uma ou mais threads._

**Processos são sequências de instruções ligadas a um software.**
_Já os threads formam conjuntos menores de intruções dentro de uma grande tarefa_.

_O que é MultiThreading?_ é um conceito em que dois ou mais threads são executados simultâneamente para aumentar a eficiência de um sistema.
_E como isso funciona?_ Básicamente cada thread é direcionada a um núcleo do processador para que isso ocorra.

_E o MultiThreading simultaneo(SMT)?_ é uma _técnica_ que permite que **múltiplos threads sejam executados ao mesmo tempo em um único núcleo do processador**.
_Tá, como funciona?_ O SMT faz os _núcleos **FÍSICOS**_ do processador serem dividos em núcleos virtuais.

#### O hyper-Threading

_O que é?_ é o mecanismo de SMT da intel.
_E serve pra que?_ Serve para permitir que a CPU tenha sua eficiencia aumentada, assim executando duas threads ao mesmo tempo em cada núcleo.

### Vantagens das threads

* Aumento da velocidade: A divisão de threads é um metódo que otimiza o fluxo de instruções, assim aumentando o desempenho da CPU.

* Maior Eficiência: O uso das threads diminui o risco de núcleos ficarem ociosos (sem fazer nada).

* Compartilhamento de recursos: Devido as threads estarem relacionados entre si, eles acabam por compartilhar recursos como endereçamento de memória e dados específicos.

* Controle de custos: A abordagem dos threads é capaz de reduzir custos de desenvolvimento de um chip, pois a o fluxo otimizado de execução elimina a necessidade de mais núcleos físicos.

