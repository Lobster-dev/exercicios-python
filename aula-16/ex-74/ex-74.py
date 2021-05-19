from random import randint

Numero = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'os valores sorteados foram: {Numero}')

Maior = 0
Menor = 0

for c in Numero:
    if c == Numero[0]:
        Maior = c
        Menor = c
    elif c > Maior:
        Maior = c
    elif c < Menor:
        Menor = c
print(f'o maior valor foi: {Maior}')
print(f'o menor valor foi: {Menor}')

print('')
# outra maneira de fazer o codigo

# print(f'o maior valor sorteado foi: {max(Numero)}')
# print(f'o maior valor sorteado foi: {min(Numero)}')
