def metade(value, form=False):
    half = value/2
    if form:
        a = f'R${half}'
        return a
    else:
        return half

def dobro(value,form=False):
    double = value * 2
    if form:
        a = f'R${double}'
        return a
    else:    
        return double


def aumento(porcentagem, value,form=False):
    ValorFinal = (value*(porcentagem/100)) + value
    if form:
        a = f'R${ValorFinal}'
        return a
    else:
        return ValorFinal


def diminuir(porcentagem, value,form=False):
    ValorFinal = value - (value*(porcentagem/100))
    if form:
        a = f'R${ValorFinal}'
        return a
    else:
        return ValorFinal

def moeda(value):
    formatacao = (f'R${value}')

def resumo(value, aument, dim):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<20}',end='R$')
    print(value)
    print(f'{"Dobro do preço:":<20}',end='R$')
    print(value*2)
    print(f'{"Metade do preço:":<20}',end='R$')
    print(value/2)
    print(f'{aument}{"% de aumento:":<18}',end='R$')
    aumento = value*(aument/100)
    aumento += value
    print(aumento)
    print(f'{dim}{"% de redução:":<18}',end='R$')
    diminuir = value*(dim/100)
    diminuir = value - diminuir
    print(diminuir)
    print('-'*30)