#Lista com todos os valores
Valores = [[],[]]

for c in range(0,7):
    numero = int(input(f'Digite o {c+1}° valor: '))
    if numero % 2 == 0:
        Valores[0].append(numero)
    else:
        Valores[1].append(numero)
print(f'os valores pares digitados foram: {Valores[0]}')
print(f'os valores impares digirados foram: {Valores[1]}')
