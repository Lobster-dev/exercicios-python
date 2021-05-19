valores = list()
QuantidadeValores = 0

while True:
    valores.append(int(input('Digite um valor: ')))
    QuantidadeValores += 1
    looping = input('desejá continuar [S/N]').lower().strip()
    if looping == 'n':
        break

print('')

print(valores)
print(f'Foram digitados {QuantidadeValores} valores')

valores.sort(reverse=True)

print(f'os valores em forma decrescente {valores} ')
print(f'o numero 5 foi encontrado na lista: {5 in valores}')