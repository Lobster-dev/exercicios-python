from utilidadesCEV import moeda

price = float(input('Digite um valor para ser analisado: R$'))
high = float(input('Digite o valor do aumento (em porcentagem): '))
low = float(input('Digite o valor da redução (em porcentagem): '))

moeda.resumo(price, high, low)
