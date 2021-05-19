#def maior(*num):
#    if len(num) == 0:
#        num = 0
#    print(f'Analisando os valores: {num}')
#    print(f'Foram informados {len(num)} valores')
#    maior = num[0]
#    for valor in num:
#        if valor > maior:
#            maior = valor
#    print(f'O maior informado foi: {maior}')


def maior(*num):
    valores = list()
    valores.append(num[:])

    print('Analisando os vários valores...')
    print(f'Foram informados {len(num)} valores')
    maior = valores[0]
    for numeros in valores:
        if numeros > maior:
            maior = numeros
    print(f'O maior valor digitado foi: {maior} ')
    print(f'{"-="*10}-')




maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

