valor = float(input())
notas100 = valor // 100
valor %= 100
notas50 = valor // 50
valor %= 50
notas20 = valor // 20
valor %= 20
notas10 = valor // 10
valor %= 10
notas5 = valor // 5
valor %= 5
notas2 = valor // 2
valor %= 2
moeda1 = valor // 1.00
valor %= 1.00
moeda50 = valor // 0.50
valor %= 0.50
moeda25 = valor // 0.25
valor %= 0.25
moeda10 = valor // 0.10
valor %= 0.10
moeda5 = valor // 0.05
valor %= 0.05
moeda01 = valor // 0.01
valor %= 0.01
print(f'NOTAS:\n{notas100:.0f} nota(s) de R$ 100.00\n{notas50:.0f} nota(s) de R$ 50.00\n{notas20:.0f} nota(s) de R$ 20.00\n{notas10:.0f} nota(s) de R$ 10.00\n{notas5:.0f} nota(s) de R$ 5.00\n{notas2:.0f} nota(s) de R$ 2.00')
print(f'MOEDAS:\n{moeda1:.0f} moeda(s) de R$ 1.00\n{moeda50:.0f} moeda(s) de R$ 0.50\n{moeda25:.0f} moeda(s) de R$ 0.25\n{moeda10:.0f} moeda(s) de R$ 0.10\n{moeda5:.0f} moeda(s) de R$ 0.05\n{moeda01:.0f} moeda(s) de R$ 0.01')