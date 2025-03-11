# Anotações com base no curso da cisco do capitulo 1

**O que são hosts?**: Todos os computadores que estão conectados a uma rede e participam diretamente da comunicação em rede são classificados como hosts/dispositivos finais.
Básicamente o termo host referencia dispositivos na rede que recebem números(IP) para propósitos de comunicação.
O IP é o número que identifica o host dentro de uma rede específica, o IP também identifica o host e a rede ao qual o host está conectado.

**O que são servidores?**: Servidores são computadores com softwares que permitem fornecer informações, como páginas web, para os dispositivos finais.
Cada serviço exige um software do servidor separado
Como mencionado anteriormente, os clientes são um tipo de host. Os clientes têm software para solicitar e exibir as informações obtidas do servidor

**software cliente** = software que requisita informações do Servidor/HOST

É possível que um mesmo mesmo computador, execute ambas as funções simultaneamente, operadando como um host e cliente, esse tipo de rede é chamada de rede ponto a ponto.

**Vantagens da rede _ponto a ponto_**

Fácil de configurar;
Menos complexo;
Menor custo porque os dispositivos de rede e os servidores dedicados podem não ser necessários;
Pode ser usada para tarefas simples como transferir arquivos e compartilhar impressoras

**Desvantagens**

Nenhuma administração centralizada;
Não é tão segura;
Não é escalável;
Todos os dispositivos podem atuar como clientes e servidores, podendo deixar seu desempenho lento.

### Voltando a falar dos dispositivos finais

Quando um dispositivo final inicia a comunicação, ele usa o endereço do dispositivo final de destino para especificar onde entregar a mensagem.

_Um dispositivo final é a origem ou o destino de uma mensagem transmitida pela rede._

Os dados se originam de um dispositivo final, fluem peça rede e terminam em outro dispositivo final.

mensagens (que são os dados enviados pela rede) podem seguir rotas alternativas.

### Dispositivos intermediarios

Esses dispositivos são responsáveis por conectar os dispositivos finais indivduais a rede. Assim eles também podem conectar várias redes individuais para formar uma internetwork. uma de suas principais responsábilidades é oferer conectividade e assegurar que os dados fluam pela rede.

Os dispositivos intermediarios usam o endereço do dispositivo final de destino, junto as informações das interconexões de rede, para informar o caminho que as mensagens devem percorrer na rede.

**algumas das funções dos dispositivos intermediarios**

Regenerar e retransmitir sinais de comunicação;
Manter informação sobre quais caminhos existem pela rede e pela rede interconectada;
Notificar outros dispositivos sobre erros e falhas de comunicação;
Direcionar dados por caminhos alternativos quando houver falha em um link;
Classificar e direcionar mensagens de acordo com as prioridades;
Permitir ou negar o fluxo de dados, com base em configurações de segurança.

**Observação:** Não mostrado é um hub Ethernet herdado. Um hub Ethernet também é conhecido como repetidor multiporta. Os repetidores regeneram e retransmitem sinais de comunicação. Observe que todos os dispositivos intermediários executam a função de um repetidor.


### Meios de rede

A comunicação transmite através de uma rede na mídia. A mídia fornece o canal pelo qual a mensagem viaja da origem ao destino.

#### Os 3 principais tipos de midia para interconectar dispositivos

Fios de metal dentro de cabos - Os dados são codificados em impulsos elétricos.
Fibras de vidro ou plástico nos cabos (cabo de fibra óptica) - Os dados são codificados em pulsos de luz.
Transmissão sem fio - Os dados são codificados através da modulação de frequências específicas de ondas eletromagnéticas.

##### Os 4 critérios principais para a escolha de mídia

Qual é a distância máxima pela qual o meio físico consegue carregar um sinal com êxito?
Qual é o ambiente em que a mídia será instalada?
Qual é a quantidade de dados e a que velocidade deve ser transmitida?
Qual é o custo do meio físico e da instalação?

## Representações e topologias de rede

Arquitetos e administradores de rede devem ser capazes de mostrar como suas redes serão.
Um diagrama fornece uma maneira fácil de entender como os dispositivos se conectam em uma rede grande.

Além dessas representações, é utilizada terminologia especializada para descrever como cada um desses dispositivos e mídias se conectam:

**Placa de interface de rede (NIC)** - Uma NIC conecta fisicamente o dispositivo final à rede.
**Porta física** - Um conector ou tomada em um dispositivo de rede onde a mídia se conecta a um dispositivo final ou outro dispositivo de rede.
**Interface** - Portas especializadas em um dispositivo de rede que se conectam a redes individuais. Como os roteadores conectam redes, as portas em um roteador são chamadas de interfaces de rede.

**Observação**: Os termos porta e interface são freqüentemente usados alternadamente.

Os diagramas de topologia são documentação obrigatória para qualquer pessoa que trabalhe com uma rede.

Existem 2 tipos de diagramas de topologia, os diagramas físicos e os lógicos.
Sendo que os Os diagramas de topologia física ilustram a localização física dos dispositivos intermediários e a instalação dos cabos.
Já os diagramas de topologia lógica ilustram dispositivos, portas e o esquema de endereçamento da rede.

## Os tipos de rede

Existem redes de vários tamanhos. Eles variam de redes simples compostas por dois computadores a redes que conectam milhões de dispositivos.

As redes domésticas simples permitem que você compartilhe recursos, como impressoras, documentos, imagens e música, entre alguns dispositivos finais locais.

As redes de pequeno escritório e escritório doméstico (SOHO) permitem que as pessoas trabalhem em casa ou em um escritório remoto.

Empresas e grandes organizações usam redes para fornecer consolidação, armazenamento e acesso a informações em servidores de rede.

## Lans e Wans

As infra-estruturas de rede variam muito em termos de:

Tamanho da área coberta;
Número de usuários conectados;
Número e tipos de serviços disponíveis;
Área de responsabilidade.

Os dois tipos mais comuns de infraestruturas de rede são as redes locais (LANs) e as redes de longa distância (WANs). 

Uma LAN é uma infraestrutura de rede que fornece acesso a usuários e dispositivos finais em uma pequena área geográfica. Normalmente, uma LAN é usada em um departamento dentro de uma empresa, uma casa ou uma rede de pequenas empresas. 

Uma WAN é uma infraestrutura de rede que fornece acesso a outras redes em uma ampla área geográfica, que normalmente pertence e é gerenciada por uma corporação maior ou por um provedor de serviços de telecomunicações. 

**Caracteristicas das LANs**

LANs interconectam dispositivos finais em uma área limitada, como uma casa, uma escola, um edifício de escritórios ou um campus.

Uma LAN é geralmente administrada por uma única organização ou pessoa. O controle administrativo é imposto no nível da rede e governa as políticas de segurança e controle de acesso.

As LANs fornecem largura de banda de alta velocidade para dispositivos finais internos e dispositivos intermediários, conforme mostrado na figura.

**Caracteristicas das WANs**

As WANs geralmente são gerenciadas por provedores de serviços (SPs) ou provedores de serviços de Internet (ISPs).

As WANS interconectam as LANs em grandes áreas geográficas, como entre cidades, estados, províncias, países ou continentes.

As WANs são geralmente administradas por vários prestadores de serviço.

As WANs geralmente fornecem links de velocidade mais lenta entre as LANs.

## A internet

A internet é uma coleção mundial de redes interconectadas (internetworks, ou internet para abreviar).

As WANs podem se conectar através de fios de cobre, cabos de fibra ótica e transmissões sem fio 

### Intranets e Extranets

Intranet é um termo frequentemente usado para se referir a uma conexão privada de LANs e WANs que pertence a uma organização. Uma intranet é projetada para ser acessada apenas por membros da organização, funcionários ou outras pessoas autorizadas.

Uma organização pode usar uma extranet para fornecer acesso seguro e protegido a indivíduos que trabalham para uma organização diferente, mas exigem acesso aos dados da organização.

**Exemplos de Extranet:**

Uma empresa que fornece acesso a fornecedores e contratados externos;
Um hospital que fornece um sistema de reservas aos médicos para que eles possam marcar consultas para seus pacientes;
Um escritório local de educação que está fornecendo informações sobre orçamento e pessoal às escolas de seu distrito.

### Formas de Acesso a Internet

Usuários domésticos, trabalhadores remotos e pequenos escritórios geralmente exigem uma conexão com um ISP para acessar a Internet.

**Opções Populares desse tipo de conexão para usuários domésticos e pequenos negócios:** incluem banda larga a cabo, a banda larga via digital subscriber line (DSL), WANs sem fio e serviços de telefonia móvel celular.

As organizações geralmente precisam acessar outros sites corporativos e a Internet. Conexões rápidas são necessárias para dar suporte a serviços comerciais que incluem telefones IP, videoconferência e armazenamento em data center. As controladoras oferecem interconexões de nível empresarial.

**Opções populares de conexão para grandes negócios e etc:** incluem DSL, linhas dedicadas e Metro Ethernet.

### Conexões de internet para casas e pequenos escritórios


**Cabo** - Normalmente oferecido por provedores de serviços _de televisão a cabo_, _o sinal de dados da Internet transmite no mesmo cabo que fornece televisão a cabo_. Ele fornece _alta largura de banda_, _alta disponibilidade_ e uma _conexão sempre ativa à Internet_.

**DSL** - As linhas de assinante digital também fornecem _alta largura de banda_, _alta disponibilidade_ e uma _conexão sempre ativa à Internet_. O DSL _funciona utilizando a linha telefônica_. Em geral, usuários de pequenos escritórios e escritórios domésticos se conectam com o uso de _DSL Assimétrico (ADSL)_, o que significa que _a velocidade de download é maior que a de upload_.

**Celular(básicamente os dados moveis)** - O acesso celular à Internet usa uma _rede de telefonia celular para se conectar_. Onde quer que você possa obter um sinal de celular, você pode obter acesso à Internet por celular. O desempenho é **limitado** pelos _recursos do telefone e da torre de celular à qual está conectado_.

**Satélite** - A disponibilidade do acesso à Internet via satélite é um _benefício_ nas áreas que, de outra forma, _não teriam_ conectividade com a Internet. As _antenas parabólicas exigem uma linha de visão clara_ para o satélite.

**Conexão Discada (Dial-up)** - Uma opção de **baixo custo** que usa _qualquer linha telefônica e um modem_. A _baixa largura de banda_ fornecida por uma conexão de modem dial-up _não é suficiente_ para grandes transferências de dados, embora seja útil para acesso móvel durante a viagem.

A escolha da conexão varia dependendo da localização geográfica e da disponibilidade do provedor de serviço

### Conexões corporativas para a internet

As empresas podem exigir _largura de banda maior_, _largura de banda dedicada e serviços gerenciados_. As opções de conexão disponíveis diferem dependendo do **tipo de provedor de serviços** localizado nas proximidades.

**Linha Alugada Dedicada** - As **linhas alugadas** são _circuitos reservados na rede do provedor de serviços_ que _conectam escritórios_ geograficamente separados para _redes privadas de voz e / ou dados_. Os circuitos são alugados a uma taxa mensal ou anual.

**Metro Ethernet** - Isso às vezes é conhecido como Ethernet WAN. Neste módulo, vamos nos referir a ele como Metro Ethernet. As ethernet metropolitanas estendem a tecnologia de acesso à LAN na WAN. Ethernet é uma tecnologia de LAN que você aprenderá em um módulo posterior.

**DSL de negócios** - O DSL comercial está disponível em vários formatos. Uma escolha popular é a linha de assinante digital simétrica (SDSL), que é semelhante à versão DSL do consumidor, mas fornece uploads e downloads nas mesmas velocidades altas.

**Satélite** - O serviço de satélite pode fornecer uma conexão quando uma solução com fio não está disponível.

## A rede Convergente

### Redes separadas tradicionais

Considere uma escola construída há trinta anos. Naquela época, algumas salas de aula eram cabeadas para a rede de dados, a rede telefônica e a rede de vídeo para televisões. Essas redes separadas não puderam se comunicar. Cada rede usava tecnologias diferentes para transmitir o sinal de comunicação. Cada rede possuía seu próprio conjunto de regras e padrões para assegurar a comunicação bem-sucedida. Vários serviços foram executados em várias redes.

### Redes convergentes 

Diferentemente das redes dedicadas, as redes convergentes são capazes de fornecer dados, voz e vídeo entre muitos tipos diferentes de dispositivos na mesma infraestrutura de rede. Essa infraestrutura de rede usa o mesmo conjunto de regras, os mesmos contratos e normas de implementação. As redes de dados convergentes transportam vários serviços em uma rede.

## Arquitetura de redes

confiabilidade significa mais do que sua conexão à Internet.

Para que as redes funcionem com eficiência e cresçam nesse tipo de ambiente, a rede deve ser construída sobre uma arquitetura de rede padrão.

Elas devem operar sobre muitos tipos diferentes de cabos e dispositivos, que compõem a infraestrutura física.

O termo arquitetura de redes, neste contexto, refere-se às tecnologias que apoiam a infraestrutura e os serviços programados e as regras, ou protocolos, que movimentam os dados na rede.

há quatro características básicas que os arquitetos de rede devem atender para atender às expectativas do usuário:

* Tolerância a falhas;
* Escalabilidade;
* Qualidade de serviço (QoS);
* Segurança.

### Tolerancia a falhas

Uma rede tolerante a falhas é aquela que limita o número de dispositivos afetados durante uma falha. Ela foi desenvolvido para permitir uma recuperação rápida quando ocorre uma falha. 
As redes dependem de diversos caminhos para funcionar.
Se um caminho falhar, as mensagens serão instantaneamente enviadas por um link diferente. Ter vários caminhos para um destino é conhecido como redundância.

A implementação de uma rede comutada por pacotes é uma das maneiras pelas quais redes confiáveis fornecem redundância.
comutação de pacotes divide os dados do tráfego em pacotes que são roteados por uma rede compartilhada.
Cada pacote tem as informações de endereço necessárias da origem e do destino da mensagem. Os roteadores na rede alternam os pacotes com base na condição da rede no momento. Isso significa que todos os pacotes em uma única mensagem podem seguir caminhos muito diferentes para o mesmo destino.

### Escalabilidade

Uma rede escalável se _expande rapidamente_ para **oferecer suporte a novos usuários e aplicativos**.
Ele faz isso _sem degradar o desempenho_ dos serviços que estão sendo acessados por usuários existentes.
Essas redes _são escaláveis porque_ os projetistas **seguem padrões e protocolos aceitos**. Isso permite que os fornecedores de software e hardware se concentrem em melhorar produtos e serviços sem precisar criar um novo conjunto de regras para operar na rede.
Usuários adicionais e redes inteiras podem ser conectados à Internet sem reduzir o desempenho para usuários atuais.

### Qualidade dos serviços

A qualidade do serviço _(QoS) é um requisito crescente das redes atualmente_.
o QoS se torna um mecanismo essencial para _gerenciar os congestionamentos_ e **garantir a entrega confiável do conteúdo para todos os usuários**.
O _congestionamento acontece_ quando a **demanda por largura de banda excede a quantidade disponível**.
A largura de banda **é medida pelo número de bits** que podem ser transmitidos em um único segundo, ou _bits por segundo (bps)_.
Ao tentar uma _comunicação simultânea pela rede_, a _demanda pela largura de banda_ pode exceder sua disponibilidade, criando um congestionamento na rede.

Quando o _volume de tráfego é maior do que o que pode ser transportado pela rede_, os dispositivos **retêm os pacotes na memória até que os recursos estejam disponíveis** para transmiti-los.

A qualidade de serviço, _controlada pelo roteador_, garante que as prioridades sejam _correspondentes ao tipo de comunicação_ e à sua importância para a empresa.

### Segurança da Rede

Os administradores de rede devem abordar _dois tipos de preocupações de segurança_ de rede: _segurança da infraestrutura de rede_ e **segurança da informação**.

Proteger a infraestrutura de rede inclui _proteger fisicamente os dispositivos que fornecem conectividade de rede_ e _impedir o acesso não autorizado ao software de gerenciamento que reside neles_.

Os administradores podem proteger a rede com segurança de software e hardware e impedindo o acesso físico aos dispositivos de rede.

Os administradores de rede também devem proteger as informações contidas nos pacotes transmitidos pela rede e as informações armazenadas nos dispositivos conectados à rede. Para atingir os objetivos de segurança de rede, **existem três requisitos principais**:

**Confidencialidade** - Confidencialidade dos dados significa que apenas os destinatários pretendidos e autorizados podem acessar e ler dados.
**Integridade** - A integridade dos dados garante aos usuários que as informações não foram alteradas na transmissão, da origem ao destino.
**Disponibilidade** - A disponibilidade de dados garante aos usuários acesso oportuno e confiável aos serviços de dados para usuários autorizados.
