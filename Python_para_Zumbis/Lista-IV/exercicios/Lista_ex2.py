from random import randint

valores = list()

for c in range(0,20):
    number = randint(1,100)
    valores.append(number)

par = list()
impar = list()
for numeros in valores:
    if numeros % 2 == 0:
        par.append(numeros)
    else:
        impar.append(numeros)

print(f'''Os valores sorteados foram: {valores}
Os valores pares são: {par}
Os valores impares são: {impar}''')