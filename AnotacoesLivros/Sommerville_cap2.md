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