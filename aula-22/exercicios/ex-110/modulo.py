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