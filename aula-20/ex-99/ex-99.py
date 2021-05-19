def maior(*num):
    if len(num) == 0:
        num = 0
    print(f'Analisando os valores: {num}')
    print(f'Foram informados {len(num)} valores')
    maior = num[0]
    for valor in num:
        if valor > maior:
            maior = valor
    print(f'O maior informado foi: {maior}')

def formatacao():
    print(f"{'-='*10}-")


formatacao()
maior(2,9,4,5,7,1)
formatacao()
maior(4,7,0)
formatacao()
maior(1,2)
formatacao()
maior(6)
formatacao()

