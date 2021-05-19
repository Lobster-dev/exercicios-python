n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))

Valores = (n1,n2,n3,n4)

print(f'os valores digitados foram: {Valores}')

print(f'O numero 9 apareceu {Valores.count(9)} vezes')

# Valores.count(3) == 0
if 3 in Valores :
    print(f'O digito 3 foi digitado na posição: {Valores.index(3)+1}')
else:    

    print('O digito 3 não foi encontrado em nenhuma posição')

print('ov valores pares giditados foram: ' , end='')
for n in Valores:
    if n % 2 == 0:
        print(n, end=' ')
