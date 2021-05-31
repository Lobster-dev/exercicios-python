import modulo

price = int(input('Digite um valor para ser analisado: R$'))
high = int(input('Digite o valor do aumento (em porcentagem): '))
low = int(input('Digite o valor da redução (em porcentagem): '))

modulo.resumo(price, high, low)
