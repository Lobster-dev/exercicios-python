valores = list()
while True: 
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero) 
        print('valor adicionado com sucesso...')
    else:
        print('Valor já existente')
    looping = input('desejá continuar [S/N]: ').lower().strip()
    if looping == 'n':
        break

print('-=-'*15)
print(f'os valores digitados foram: {valores} ')
valores.sort()
print(f'os valores em ordem crescente: {valores}')