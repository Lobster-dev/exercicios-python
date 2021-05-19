#Tuplas (Variaveis compostas)
# AS TUPLAS SÃO IMUTAVEIS
#tuplas são entre parenteses ()

lanche = ('Hamburguer','Suco' ,'Pizza' ,'Pudim')
print('Lanche: ',lanche)
print('Lanche 1:',lanche[1])
print('Lanche 1:3 :',lanche[1:3])
print('lanche[:2]',lanche[:2])

print('')

#maneira de escrever de um jeito formatado bonitinho, sem parenteses e virgulas
for comida in lanche:
    print(comida)
#Outra maneira de fazer a mesma coisa porem usando o comando range
#for comida in range(0 , len(lanche)):
#    print(lanche[comida])

#for pos, comida in enumerate(lanche):
#    print(f'eu vou comer {comida}n na posição {pos}')

print('')

#escreve em ordem
print(sorted(lanche))

print('')

a = (1,2,3,4,5)
b = (5,6,7,8,9)
c = a + b
print(c)
#conta quantas vezes o que está entre parenteses aparece
print(c.count(5))
#mostra a posição do objeto entre parenteses (a 1° ocorrencia do número)
print(c.index(8))
#procurá aonde aparece o digito 5 apartir da posição 5 
print(c.index(5,5))

print('')

#pode ter elementos diversos dentro dele
pessoa = ('Gustavo', 39, "aws", 99.5)
# apaga a tupla 
del(pessoa)
print(pessoa)
