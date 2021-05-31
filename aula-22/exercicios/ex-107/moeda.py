def metade(value):
    half = value/2
    return half

def dobro(value):
    double = value * 2   
    return double


def aumento(porcentagem, value):
    ValorFinal = (value*(porcentagem/100)) + value
    return ValorFinal

def diminuir(porcentagem, value):
    ValorFinal = value - (value*(porcentagem/100))
    return ValorFinal