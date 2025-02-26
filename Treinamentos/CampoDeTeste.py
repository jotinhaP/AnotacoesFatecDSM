valores = input().split(' ')
valor_A = int(valores[0])
valor_B = int(valores[1])
valor_C = int(valores[2])
maior_AB = (valor_A + valor_B + abs(valor_A - valor_B)) / 2
maior_ABC = (maior_AB + valor_C + abs(maior_AB - valor_C)) / 2
print(f'{maior_ABC:.0f} eh o maior')
