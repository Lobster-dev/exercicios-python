valores = list()
pares = list()
impares = list()

while True: 
    numero = int(input('Digite um valor: '))
    valores.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 != 0:
        impares.append(numero)
    looping = input('Desejá continuar [S/N]: ').lower().strip()
    if looping == 'n':
        break    
print('-=-'*10)
print(f'os numeros digitados foram: {valores} \nDentre esses valores são pares: {pares} \nSão impares os valores: {impares}')




