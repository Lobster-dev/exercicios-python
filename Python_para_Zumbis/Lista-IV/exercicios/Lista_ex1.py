from random import randint

numeros = list()

for c in range(0,10):
    n = randint(1,100)
    numeros.append(n)

maior = menor = numeros[0]

for valor in numeros:
    if maior < valor:
        maior = valor
    if menor > valor:
        menor = valor

print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor digitado foi: {maior}\nO menor valor digitado foi: {menor}')