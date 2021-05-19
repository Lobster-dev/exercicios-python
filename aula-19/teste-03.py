
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'Sao Paulo', 'sigla':'SP'}
brasil = list()
brasil.append(estado1)
brasil.append(estado2)

print ('')

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

del brasil
print('')

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = input('uf: ')
    estado['sigla'] = input('sigla: ')
    print('')
    # para fazer uma coipia de um dicionario usa-se o metodo .copy()
    brasil.append(estado.copy())

for e in brasil:
    print(e)
    for k,v in e.items():
        print(f'o campo {k} trem valor {v}')
    print('')
    
    