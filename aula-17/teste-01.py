# listas
# são semelhantes as tuplas 
# porem elas podem ser alteradas
# listas utilizam o sinal [] para definir listas

Lanche = ['HAMBURGUER', 'SUCO', 'PIZZA', 'BATATA-FRITA','PUDIM']
for comida in Lanche:
    print(comida)
Lanche[3] = 'PICOLE'
print(Lanche[3])

print('')

#para adicionar itens em uma lista usa-se o comando .append('elemento') adiciona no final da lista
# para inserir itens no meio da lista usa-se o comando .insert(posição do item,'nome do item')
Lanche.insert(0,'CACHORRO-QUENTE')

for comida in Lanche:
    print(comida)

print('')

#para apagar itens na lista usa-se o comando del ou o comando .pop(numero do elemento)
#ex: 
Lanche.insert(5,'INEXISTENTE')
for comida in Lanche:
    print(comida)
print('')
del Lanche[5]
print(Lanche)

print('')

#para remover o elemento usando o valor inserido nele usa-se o comando .remove('elemento')
#usando o comanod .pop[] mas sem identificar o elemento, é removido o ultimo elemento da lista

# cria uma lista com os valores de 4 até 10 
valor = list(range(4,11))
print(valor)

#para colocar os elementos em ordem crescente usa-se o comando .sort()
#para ordenar os valores em ordem drecrescente usa-se o comando .sort(reverse=True)
#a função len() tamém funciona em uma lista para saber o tamanho

