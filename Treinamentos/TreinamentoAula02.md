# Anotações sobre o Segundo treinamento interfatecs e tal

Caso por alguma razão a gente precise deixa o final de uma linha no python diferente da quebra de linha padrão, nós usamos o _end_, assim no final da linha ela não vai quebrar e vai imprimir o que a gente mandar.
**EX:** print('morri', end='X-X')

Uma explicação sobre a formatação de váriaveis nas F strings e tal, temos por exemplo essa exibição aqui num print: {valor:.4f}.
valor é a váriavel a ser mostrada
O ":" Indica que queremos editar essa várivel
O ".4" indica que queremos indicar as casas após a virgula
E o "f" está indicando que esses valores após a virgula são de uma váriavel float

A função _.strip()_ remove os espaços extras antes e depois de uma string, caso nós desejemos remover caracteres específicos de uma string, podemos passar tais caracteres como parametros dessa função _EX:texto.strip('ae')_

A função _.split()_ permite dividir uma string em substrings com base em um delimitador específico.
Essa função pode receber dois parametros, um deles sendo o _"sep"_, que é o caractere que definimos como o delimitador base do split, ou seja _se definirmos o "."_ como o delimitador a string será cortada nesses pontos.
E o parametro "_maxsplit_", que é o numero máximo de partes que essa string pode ser dividida.
EX: frase = Olá, tudo bem?
    frase.split(",", maxsplit=2)
**OBS: ambos esses parametros são opcionais, no caso do sep, caso ele não seja definido os espaços em branco serão os delimitadores**