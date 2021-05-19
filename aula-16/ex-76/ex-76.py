
Lista = ('Lápis',1.75,
    'Borracha',2,
    'Caderno',15.90,
    'Penal',25,
    'trasferidor',4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.9)

print('-'*40)
print('{:^40}'.format('listagem de preços').upper())
print('-'*40)

for Produto in range (0,len(Lista)):
    if Produto % 2 == 0:
        print(f'{Lista[Produto]:.<31}', end='R$')
    else:
        print(f'{Lista[Produto]:0.2f}')

print('-'*40)