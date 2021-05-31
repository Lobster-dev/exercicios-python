from utilidadesCEV import moeda

price = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(price)} é {moeda.moeda(moeda.metade(price))}')
print(f'O dobro de {moeda.moeda(price)} é {moeda.moeda(moeda.dobro(price))}')
print(f'Aumentando 10% temos: {moeda.moeda(moeda.aumento(10,price))}')
print(f'Diminuindo 13% temos: {moeda.moeda(moeda.diminuir(13,price))}')
