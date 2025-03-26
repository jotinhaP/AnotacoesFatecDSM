# Anotações baseadas no cap 1.1.1 até o cap

## Defesa em profundidade

### ativos, Vulnerabilidades e Ameaças

**Ativos** São qualquer coisa de valor para uma organização que deve ser protegida, incluindo servidores, dispositivos de infraestrutura, dispositivos finais e o maior ativo, dados.
**Vulnerabilidades** É uma fraqueza em um sistema ou em seu design que pode ser explorada por um agente de ameaça.
**Ameaças** São qualquer perigo potencial para um ativo.

### Identificar Alvos

Muitas organizações só têm uma ideia geral dos ativos que precisam ser protegidos.

A coleta de todos os dispositivos e informações de propriedade ou gerenciadas pela organização são ativos. Os ativos constituem a superfície de ataque que os atores da ameaça podem atingir.
Por isso é necessario inventariar/classificar o nivel necessário de proteção para cada um desses ativos.

O gerenciamento de ativos consiste em inventários de todos os ativos e, em seguida, desenvolver e implementar políticas e procedimentos para protegê-los. 

Além disso, as organizações precisam identificar onde os ativos de informações essenciais estão armazenados e como o acesso é obtido a essas informações. Os ativos de informação variam, assim como as ameaças contra eles.

### Classificação dos Ativos

A classificação de ativos atribui todos os recursos de uma empresa a um grupo, com base em características comuns. As informações mais importantes precisam receber o nível mais alto de proteção e ainda podem exigir um tratamento especial.

Uma empresa pode adotar um sistema de rotulagem, de acordo com o valor, a confidencialidade e a importância das informações.

**Primeira Etapa:** Determinar em qual categoria os ativos se encaixam, sendo elas _ativos de informação_, _ativos de software_, _ativos físicos_, _Serviços_.
**Segunda Etapa:** Estabelecer a responsabilização, indentificar o proprietario de todos os ativos de tipo, _informação_ e _software de aplicação_
**Terceira Etapa:** Determinar os criterios de classificação
*  Confidencialidade
*  Valor
*  Tempo
*  Direitos de acesso
*  Destruição
**Quarta Etapa:** Implementar um esquema de classificação, adote uma maneira uniforme de identificar as informações para garantir uma segurança uniforme.

### Padronização de Ativos

Os padrões do ativo identificam produtos de hardware e software específicos usados e suportados pela empresa.
Essa padronização facilita a ação imediata caso ocorra algum erro, caso uma empresa não padronize a seleção de hardware será mais dificil encontrar um componente para reposição.
Além de _exigirem mais conhecimento_ para serem gerenciados, ambientes não padronizados _aumentam o custo com contratos de manutenção e inventário._

### Estágios de ciclo de vida de um ativo

1 - **Aquisição**: A empresa compra o ativo com base nas necessecidades identificadas nos seus dados, para justificar a compra, assim adicionando o ativo ao inventário da empresa.
2 - **Implantação**: O ativo é analisado para conferir se não há falhas ou outros problemas, assim são realizados testes, tags/codigos de barra são instalados para rastreamento, o ativo passa do inventário para em uso.
3 - **Utilização**: Essa é a fase mais longa, pois o ativo tem costantemente seu desempenho verificado, Atualizações, correções de patches, compras de novas licenças e auditorias de conformidade fazem parte do estágio de utilização.
4 - **Manutenção**: A manutenção possibilita aumentar a vida produtiva de um ativo, assim os funcionarios podem atualizar o recurso.
5 - **Eliminação**: No fim da vida produtiva do ativo, ele é descartado. Assim apagando todos os dados do recurso. caso seja um ativo físico ele pode ser desmontado em peças. As peças que podem casar problemas ambientais são descartadas de acordo com as diretrizes locais.

### identificando vulnerabilidades

Identificar ameaças possibilita uma oragnização fazer uma lista de prováveis ameaças para um ambiente específico.
Algumas perguntas a se fazer:
Quais são as possíveis vulnerabilidades de um sistema?
Quem pode querer explorar essas vulnerabilidades para acessar ativos de informações específicos?
Quais são as consequências se as vulnerabilidades do sistema forem exploradas e os ativos forem perdidos?

**Exemplo: identificação de ameaças para um sistema de banco eletronico**
_Compromisso interno do sistema_ - O atacante usa os servidores de e-banking expostos para invadir um sistema bancário interno.
_Dados roubados do cliente_ - Um atacante rouba os dados pessoais e financeiros dos clientes bancários do banco de dados do cliente.
_Transações falsas de um servidor externo_ - Um invasor altera o código do aplicativo de e-banking e faz transações personificando um usuário legítimo.
_Transações falsas usando um PIN de cliente roubado ou cartão inteligente_ - Um invasor rouba a identidade de um cliente e conclui transações mal-intencionadas da conta comprometida.
_Ataque insider no sistema_ - Um funcionário do banco encontra uma falha no sistema a partir do qual montar um ataque.
_Erros de entrada de dados_ - Um usuário insere dados incorretos ou faz solicitações de transação incorretas.
_Destruição do data center_ - Um evento cataclísmico danifica gravemente ou destrói o data center.

### Identifique as ameaças

As abordagens de defesa, devem ser profundas sendo compostas de várias camadas de segurança na borda da rede e nas suas extremidades

Exemplo de topologia simples de uma abordagem de defesa de profundidade:

_Roteador de borda_ - A primeira linha de defesa é conhecida como um roteador de borda. O roteador de borda tem um conjunto de regras especificando qual tráfego ele permite ou nega. Ele passa todas as conexões que se destinam à LAN interna para o firewall.

_Firewall_ - A segunda linha de defesa é o firewall. O firewall é um dispositivo de ponto de verificação que executa filtragem adicional e rastreia o estado das conexões. Ele nega o início de conexões de redes externas (não confiáveis) para a rede interna (confiável), enquanto permite que usuários internos estabeleçam conexões bidirecionais com as redes não confiáveis. Ele também pode executar autenticação de usuário (proxy de autenticação) para conceder aos usuários remotos externos acesso a recursos de rede interna.

_Roteador interno_ - Outra linha de defesa é o roteador interno. Ele pode aplicar regras de filtragem finais no tráfego antes de ser encaminhado para seu destino.

_Alguns outros dispositivos usados na abordagem de defesa profunda seriam_: IPS (Intrusion Prevention Systems), Proteção Avançada contra Malware (AMP), sistemas de segurança de conteúdo da Web e de e-mail, serviços de identidade, controles de acesso à rede e etc.

Na abordagem de segurança em camadas de defesa profunda, as diferentes camadas trabalham juntas para criar uma arquitetura de segurança na qual a falha de uma salvaguarda não afeta a eficácia das outras salvaguardas.

### Algumas analogias para a abordagem de defesa em profundidade

#### Cebola de segurança

Essa analogia é usada, pois, assim como uma cebola um ator de ameaça teria que "descascar" as defesas da rede camada por camada. Pois somente depois de "descascar" todas as camadas ele alcançaria os dados.
A Security Onion descrita nesta página é uma forma de visualizar a defesa em profundidade. Isso não deve ser confundido com o conjunto Security Onion de ferramentas de segurança de rede.

**Defesas:** 
* Dispositivos endurecidos
* Autenticação, Autorização, and Contabilidade (AAA)
* Filtragem de conteúdo
* Intrusion Prevention Systems (IPS)
* Firewall 

#### Alcachofra de segurança

Atualmente com a evolução da rede sem fronteiras, acabou mudando essa analogia da cebola, pois os atores de ameaça acabam por ser mais beneficiados.

Nesse caso os atores da ameaça não precisam mais descascar cada camada. Eles só precisam remover certas “folhas de alcachofra”. O bônus é que cada “folha” da rede pode revelar dados confidenciais que não estão bem protegidos.

Por exemplo, é mais fácil para um agente de ameaça comprometer um dispositivo móvel do que comprometer um computador ou servidor interno protegido por camadas de defesa. Cada dispositivo móvel é uma folha. E folha após folha, tudo leva o hacker a mais dados. O coração da alcachofra é onde os dados mais confidenciais são encontrados. Cada folha fornece uma camada de proteção enquanto fornece simultaneamente um caminho para o ataque.

### Estrategias de Defesa em Profundidade

O ideal é que empresas usem mais de uma estrategia para defesa, para que assim a segurança fique mais atenuada, assim garantindo que as informações e dados continuem disponiveis, por isso empresas tem a necessidade de criar diferentes camadas de proteção.

**Sobreposição**:  Um bom exemplo de camadas é uma empresa que armazena seus documentos ultra-secretos em um servidor protegido por senha em um prédio trancado e cercado por uma cerca elétrica.

**Limitação**: Limitar o acesso aos dados e às informações reduz a possibilidade de uma ameaça. Uma empresa deve restringir o acesso para que os usuários tenham apenas o nível de acesso necessário para fazer o seu trabalho. Uma empresa deve ter as ferramentas e as configurações certas, como permissões de arquivo, para limitar o acesso, bem como as medidas processuais certas, que definem etapas específicas para fazer qualquer coisa que possa afetar a segurança.

**Diversidade**: Basicamente as camadas de segurança precisam ser diferentes umas das outras, pois obviamente se um invasor penetrou um tipo de defesa, ter uma defesa igual só facilitaria o trabalho dele. Usar diferentes algoritmos e sistemas é uma ótima forma de fortalecer sua defesa, assim é possivel defender os dados nas mais variadas circunstãncias.
Para tornar essa diversidade ainda maior, uma empresa pode usar produtos de segurança de empresas distintas, como por exemplo ter um cartão de furo de uma empresa e um leitor digital de outra.

**Ofuscação**: Ofuscar dados, é uma medida importante de segurança, pois quanto menos os satacantes souberem do seu sistema, fica mais difícil a formulação de um ataque, por isso empresas não revelam informações como versões dos SOs que estão em servidores ou o tipo de equipamento usado.

**Simplicidade**: Complexidade não garante segurança, muitas vezes pode ocorrer o contrário, o sistema pode ser tão complexo que realizar manutenções nele fique algo muito difícil e demorado. O ideal é que esse sistema de defesa seja simples para o ponto de vista dos funcionários e complexo para quem está no meio externo.

## Gerenciamento de Operações de segurança cibernética

### Gerenciamento de configurações

Gerenciamento de Configurações diz respeito a toda e qaulaquer alteração(identificação, controle e auditoria da implementação) feitas na linha de base de um sistema.
Configurar uma linha de base inclui todas as definições de um sistema que fornece base para todos os outros sistemas semelhantes, básicamente é uma espécie de modelo.
Um exemplo disso seria quando é necessário instalar estações de trabalho windows, nesse caso é necessário que seja instalado os aplicativos e definir as configurações do sistema de acordo com uma configuração pré-documentada.

### Arquivos de Log

Um log registra todos os eventos ocorridos, entradas de log compõem arquivos, e todas essas entradas tem informações relacionadas a um evento.
Por exemplo, um log de auditoria rastreia as tentativas de autenticação do usuário.
Monitorar os logs permite saber como um ataque ocorreu e se as defesas funcionaram.

O gerenciamento de dados do log de segurança deve determinar os procedimentos para o seguinte:
 * Gerando arquivos de log
 * Transmissão de arquivos de log
 * Armazenamento de arquivos de log
 * Análise de dados
 * Descartando dados de log

### Registros do sistema operacional e registros de segurança do aplicativo

**logs do SO**: O sistema operacional registra eventos de registro que estão vinculados a ações relacionadas ao sistema operacional. Eventos do sistema incluem o seguinte:

 * Solicitações do cliente e respostas do servidor, como autenticações de usuário bem-sucedidas

 * Informações de uso que contêm o número e o tamanho das transações em um determinado período de tempo

 **Segurança de Aplicações**: Empresas usam software de segurança pela rede ou pelo sistema para detectar atividade mal-intencionada.
 Esse software irá gerar os logs de segurança pra fornecer os dados relacionados a segurança, assim facilitando a empresa a analisar e identificar problemas e fornecer documentação que está tudo nos conformes.

### Analisadores de Protocolo

Packet anlyzers interceptam e resgistram o tráfego de rede.
Um sniffer pode capturar o tráfego e redes com e sem fio.
Os packet analyzers básicamente capturam os pacotes, mostram os valores de vários dos campos do pacote e analisa seu conteúdo.

**As Funções de um Packet analyzer:**
 * Log de tráfego
 * Análise de problemas de rede
 * Detecção de uso indevido da rede
 * Detecção de tentativas de invasão da rede
 * Isolamento do sistema explorado

