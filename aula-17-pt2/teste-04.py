galera = list()
dado = list()
totalmaior = totalmenor = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')).capitalize())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1
print(f'temos {totalmaior} pessoas maiores de idade e {totalmenor} pessoas menores de idade')    