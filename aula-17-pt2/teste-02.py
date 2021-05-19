teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

print('')

galera = list()
galera.append(teste[:])
print(galera)

print('')

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)