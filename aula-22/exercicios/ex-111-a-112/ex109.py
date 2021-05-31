from utilidadesCEV import moeda

price = float(input('Digite o preço: R$'))
while True:
    formatacao = str(input('Desejás ver os valores formatados [S/N]: ')).lower().strip()
    if formatacao == 's' or formatacao == 'n':
        break

if formatacao == 's':
    print(f'A metade de R${price} é {moeda.metade(price,True)}')
    print(f'O dobro de R${price} é {moeda.dobro(price,True)}')
    print(f'Aumentando 10% temos: {moeda.aumento(10,price,True)}')
    print(f'Diminuindo 13% temos: {moeda.diminuir(13,price,True)}')
elif formatacao == 'n':
    print(f'A metade de {price} é {moeda.metade(price)}')
    print(f'O dobro de {price} é {moeda.dobro(price)}')
    print(f'Aumentando 10% temos: {moeda.aumento(10,price)}')
    print(f'Diminuindo 13% temos: {moeda.diminuir(13,price)}')