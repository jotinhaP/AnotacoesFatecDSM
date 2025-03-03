# Anotações com base no curso da cisco

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

