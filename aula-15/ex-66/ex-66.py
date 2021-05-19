QuantNum = 0
Soma = 0

while True:
    numero = int(input('Digite um número (Digite 999 para parar): '))
    if numero == 999:
        break
    else: 
        Soma = Soma + numero
        QuantNum += 1
print(f'Foram digitados: {QuantNum} valores \nA soma entre ele é de: {Soma}')