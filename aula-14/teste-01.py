# Laços de repetição, estrutura while
for c in range (1,10):
    print(c)
print('Fim.')

print('')

contador = 1 
while contador <= 10:
    print(contador)
    contador = contador + 1
print('Fim')

print('')

r = 's'
while r == "s":
    n = int(input('Digite um valor: '))
    r = input('Quer continuar: ').lower()

print('')

n = 1
QuantNum = 0
impar = 0 
par = 0
while n != 0:
    n = int(input('Digite um valor'))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    QuantNum = QuantNum + 1
print('Você digitou {} numeros e dentre eles {} são pares e {} são impares'.format(QuantNum, par, impar))