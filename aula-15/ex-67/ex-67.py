

while True:
    contador = 1
    numero = int(input('Digite um numero para ver a sua tabuada: '))
    if numero >=0:
         while contador <= 10:
            print(f'{numero} x {contador} = {numero*contador}')
            contador += 1
    else: 
        break
    print('')

