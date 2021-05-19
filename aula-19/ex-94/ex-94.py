pessoa = dict()
galera = list()
soma = media = 0


while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!! por favor digitar somente M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    loop = str(input('Deseja continuar [S/N]: ')).lower()[0]
    while True:
        if loop in "sn":
            break
        print('ERRO!!Digite somente S ou N')
    if loop == 'n':
        break

print('')
print(f'{"-="*24}-')
print('')

print(galera)
print(f'Ao todo tem {len(galera)} pessoas cadastradas.')

media = soma / len(galera)

print(f'a) A média de idade é: {media:5.2f}')
print(f'b) As mulheres cadastradas foram: ', end='')

for p in galera:
    if p['sexo'] in "Ff":
        print(f'{p["nome"]}',end=" ")
print('')

contador = 0
print(f'c) As pessoas com idade acima da média foram: ')
for Pessoas in galera:
    if Pessoas['Idade'] >= media:
        print(f'{galera[contador]}',end=' ')
        contador += 1 
