#parte 2 de listas
dados = ['pedro', '25']
pessoas = list()

pessoas.append(dados[:])
pessoas.append('nome')
print(pessoas)

del pessoas

print('')

#outra maeira de escrever listas compostas é: 
pessoas = [['Pedro', '25'], ['Maria','19'], ['Joao','32']]
print(pessoas[0])

#para escrever um item de dentro de uma lisra composta usa-se 2'[]' sendo
#o 1° para expressar qual elemento da lista externa e o 2° paa expressar o elemento da lista interta
print(pessoas[0][0])

