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