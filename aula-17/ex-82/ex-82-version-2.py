valores = list()
pares = list()
impares = list()

while True: 
    valores.append(int(input('Digite um valor: ')))
    looping = input('Desejá continuar [S/N]: ').lower().strip()
    if looping == 'n':
        break 

for numero in valores:
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 != 0:
        impares.append(numero)

print('-=-'*10)
print(f'os numeros digitados foram: {valores} \nDentre esses valores são pares: {pares} \nSão impares os valores: {impares}')
