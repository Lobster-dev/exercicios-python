from random import randint
numeros = list()


def sorteia():
    for c in range(0,5):
        numeros.append(randint(0,10))
    print(f'os valores sorteados foram: {numeros}')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares é: {soma}')


sorteia()
somapar(numeros)
