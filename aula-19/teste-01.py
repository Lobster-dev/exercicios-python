# para identifiar um dicionario usa-se o comando dict() ou o simbolo {}
# estrutura do dicionario:
# Nome do dicionario = {'referencia': Valor , ...}
dados = {'nome':'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
#para adicionar outros itens na lista não necessita de um comando como nas listas(.append())
# usa-se somente a estrutura -> nome do dicionario['referencia'] = 'novo valor' 
# ex:
dados['sexo'] = 'M'
print(dados['sexo']) 

print('')

# para remover um dos dados usa-se o comando del nome do dicionario[referencia a ser deletada]

filme = {
'Titulo': 'Star Wars',
'ano': 1977,
'Diretor': 'George Lucas'        
}
print(filme['ano'])
print(filme['Titulo'])

print('')

#para escrever todos os valores usa-se o comando .values()
print(filme.values())
#para escrever as referencias (ou como o python chama "Chaves") usa-se o comando .keys()
print(filme.keys())
#para escrever tudo (valores e referencias) usa-se o comanod .items()
print(filme.items())

print('')

for key, values in filme.items():
    print(f'o {key} é {values}')

print('')

#pode-se colocar dicionarios dentro de listas
locadora = list()
filme2 = {'titulo': 'avengers', 'ano': 2012, 'diretor': 'Joss whedon'}
filme3 = {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Machowski'}
locadora.append(filme)
locadora.append(filme2)
locadora.append(filme3)
#para escrever esses valores usa-se a estrutura:
# Nome da lista[item da lista(valor numerico)][item do dicionario(key)]
print(locadora[0]['ano'])
print(locadora[1]['ano'])
print(locadora[2]['ano'])

print('')
