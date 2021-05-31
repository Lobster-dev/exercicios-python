from utilidadesCEV import moeda

price = float(input('Digite o preço: R$'))

print(f'A metade de {price} é {moeda.metade(price)}')
print(f'O dobro de {price} é {moeda.dobro(price)}')
print(f'Aumentando 10% temos: {moeda.aumento(10,price)}')
print(f'Diminuindo 13% temos: {moeda.diminuir(13,price)}')
