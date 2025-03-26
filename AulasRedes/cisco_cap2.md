# Anotações baseadas no modulo 2 do curso da cisco

# Acesso ao Cisco IOs

## Sistemas Operacionais

Todo computador, seja ele um dispositivo final ou não, necessita de um sistema operacional.
A parte do SO que interage diretamente com o hardware do computador, _se chama KERNEL_.
A parte que tem interface com aplicações para o usuário, _se chama SHELL_.
O usuário pode **interagir com a shell** por meio de uma _interface de linha de comando CLI (Interface de linha de Comando)_ ou uma _interface gráfica de usuário GUI (Interface Gráfica do Usuário)_.

Basicamente:

**Shell** - A interface de usuário que permite que os usuários solicitem tarefas específicas do computador. Essas solicitações podem ser feitas por meio da interface CLI ou GUI.
**Kernel** - comunica-se entre o hardware e o software de um computador e gerencia como os recursos de hardware são usados para atender aos requisitos de software.
**Hardware** - A parte física de um computador, incluindo os componentes eletrônicos subjacentes.

_A CLI_ exige menos do computador, por se tratar de uma interface que se baseia apenas em texto(códigos, comandos e etc), mas acaba exigindo que o usuário tenha conhecimento da estrutura de comando que controla o sistema.

## GUI

GUIs permitem que o usuário interaja mais facilmente co o sistema atráves do uso de janelas, ícones, menus e etc. Exemplos de GUI seriam linux, windows, macOS e etc.
As GUIs ajudam bastante os usuários mais leigos quanto ao funcionamento da estrutura de comando do sistema a navegarem por ele, mas nem sempre as GUIs tem todos os recursos que uma CLI
As CLI _consomem menos recursos e são muito mais estáveis_, em comparação com uma GUI.

**O sistema operacional nos roteadores domésticos geralmente é chamado firmware. O método mais comum para configurar um roteador residencial é usando uma GUI pelo navegador.**

## Objetivo de um SO

Um SO de rede baseado em CLI permite que um tecnico de rede faça o seguinte:

Use um teclado para executar programas de rede baseados na CLI;
Use um teclado para inserir texto e comandos baseados em texto;
Exibir a saída em um monitor.

Básicamente tarefas muito parecidas com o que um SO de computador comum permite.

Embora todos os dispositivos venham com o IOS e um conjunto de recursos padrão, é possível atualizar a versão do IOS ou do conjunto de recursos para obter mais capacidades.

## Metodos de Acesso

Switchs por natureza irão encaminhar o tráfego e não precisam necessáriamente ser configurados para operar, de qualquer forma **todos os switches devem ser configurados e protegidos**.

![Metodos de acesso](imagens/metodosDeAcesso)

Note: Alguns dispositivos, como roteadores, também podem suportar uma porta auxiliar herdada usada para estabelecer uma sessão CLI remotamente por uma conexão telefônica usando um modem. De modo semelhante a uma conexão de console, a porta AUX é do tipo fora de banda e não requer serviços de rede para ser configurada ou estar disponível.

# Navegação IOS

## Modos de Comandos Primários

Esse capitulo cai abordar como configurar/navegar num SO de um sistema de redes com bas ena CLI (command line interface), baseando-se no SO que a cisco tem para seus dispositivos, sendo ele o Cisco IOs

Dito iss, para medidas de segurança o software Cisco IOS separa o acesso de gerenciamento em dois modos de comando:

 * **Modo EXEC de usuário**: Este modo possui recursos limitados, mas é útil para operações básicas. Ele permite apenas um número limitado de comandos de monitoramento básicos, mas não permite a execução de nenhum comando que possa alterar a configuração do dispositivo. O modo EXEC usuário é identificado pelo prompt da CLI que termina com o símbolo >.
 
 * **Modo EXEC privilegiado**: Para executar comandos de configuração, um administrador de rede deve acessar o modo EXEC privilegiado. Modos de configuração mais altos, como o modo de configuração global, só podem ser acessados do modo EXEC privilegiado. O modo EXEC privilegiado pode ser identificado pelo prompt que termina com o # símbolo.

[Metodos e prompts](imagens/tabelaModosEPrompts.png)

## Modos de Configuração e SubConfiguração

O modo **Configuração Global** é o modo que permite _configurar os dispositivos de rede_, e seu funcionamento como um todo.
**OBS: Para indentificarmos que estamos no modo de configuração global, basta ver se no prompt a linha termina com _(config)#_** Exemplo: Swtich(config)#.

Nós acessamos modos de configuração mais específicos apartir do modo de configuração global, pois nele que inserimos modos de subConfiguração, cada modo de subConfiguração permite que nós configuremos uma parte específica do dispositivo.

Os dois modos comuns de subconfiguração são:
 * **Modo de configuração de linha**: Usado para configurar o acesso ao console, SSH, Telnet ou AUX.
 * **Modo de configuração da interface**: Usado para configurar uma porta de switch ou interface de rede do roteador.

Por padrão, todo prompt começa com após após o nome do dispositivo. Após o nome, o restante do prompt indica o modo.
EXs: o prompt padrão de configuração de linha é _Switch(config-line)#_ e para o modo interface _Switch(config-if)#._

### Como acessar esses metodos na CLI Do Cisco IOs

Para sairmos do modo EXEC usuário para privilegiado usamos o comando **enable**
E para irmos do EXEC privilegiado pro global usamos **Configure Terminal**
Para entrarmos no modo de configuração de interface usamos **interface vlan 1**
**OBS: O modo _EXEC privilegiado_ também é chamado de _enable mode_**