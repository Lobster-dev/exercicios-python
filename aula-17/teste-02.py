valores = list()
for cont in range(0,2):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

print('')

a = [2,3,4,7]
b = a
b[2] = 8
print(a)
print(b)

print('')

a = [2,3,4,7]
b = a[:]
b[2] = 8
print(a)
print(b)
