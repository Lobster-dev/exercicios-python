galera = [['JOAO', 19], ['ANA', 33], ['JOAQUIM', 13], ['MARIA', 45]]


print(galera)
print(galera[0])
print(galera[0][0])

print('')

for nome, idade in galera:
    print(nome, end='->')
    print(idade)
print('')

print('')

for nome, idade in galera:
    if idade > 20:
        print(f'{nome} tem mais de 20 anos ')
    else:
        print(f'{nome} tem menos de 20 anos')


print('')



