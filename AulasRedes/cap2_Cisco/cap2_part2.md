# Anotações baseadas no modulo 2 do curso da cisco (2.0 - 2.3)

# Configurações básicas de Dispositivo

## Nomes de dispositivo

A primeira coisa que fazemos na configuração de um dispositivo, é dar a ele um nome exclusivo ou um nome de host.
Pensa que é tipo dar nome de váriavel, seja descritivo nos nomes, eles devem ser intuitivos.

**Como aplicar o nome de um dsipositivo na CLI**:
Nós primeiro entramos no modo de configuração global.
Após isso digite o comando _hostname (nome para maquina)_.
Caso você queira tirar/esconder o nome use o comando _no hostname_

## Diretrizes de Senha

O Cisco IOS pode ser configurado para usar senhas do modo hierárquico para permitir privilégios de acesso diferentes a um dispositivo de rede.
Todos os modos da CLI e a telnet devem ter suas respectivas senhas, devem também ser criptografadas e devem fornecer notificações legais.

**Dicas para uma senha fortissima**:

 * Use senhas com mais de oito caracteres.
 * Use uma combinação de letras maiúsculas e minúsculas, números, caracteres especiais e/ou sequências numéricas.
 * Evite usar a mesma senha para todos os dispositivos.
 * Não use palavras comuns porque elas são facilmente adivinhadas.

E pra você não sofrer criando muitas senhas dessas, é só usar um gerador de senhas.

## Colocando senhas nos dispositivos

**Colocando senha no EXEC de usuário**:
 * Primeiro a gente entra no modo EXEC global;
 * Depois usamos o comando _line console 0_;
 * Depois usamos o comando _password (insira senha aqui)_;
 * Depois usamos o comando _login_ para ativar o acesso EXEC do usuário;
 * por fim use o comando _end/exit_ caso você queira sair do modo global.

Pronto agora o console vai pedir uma senha para quem for usar o EXEC de usuário.

**Colocando senha no EXEC privilegiado**:
 * Entra no modo EXEC global;
 * Usa o comando _line console 0_;
 * Usa o comando _enable secret (insira a senha aqui)_;
 * Use o comado _end/exit_ para sair do modo global se desejado.

### Configurando a senha do VTY

As linhas de terminal virtual (VTY) permitem acesso remoto usando Telnet ou SSH ao dispositivo.

**Colocando a senha no VTY**:
 * Entre no Modo EXEC global;
 * Entre no Modo VTY, usando o comando _line vty 0 15_;
 * Use o comando _password (insira senha aqui)_;
 * Use o comando _login_;
 * E se necessário use o comando _end/exit_ para sair do modo vty.

 
