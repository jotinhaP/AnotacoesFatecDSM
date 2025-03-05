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
