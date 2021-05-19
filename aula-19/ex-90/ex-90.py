situacao = {'a': 'Aprovado', 'er': 'Em Recuperação', 'r':'Reprovado' }

nome = input('Nome: ').capitalize().strip()
media = float(input(f'Média de {nome}: '))

if media <= 5:
    print(situacao['r'])
elif 5 < media <= 7:
    print(situacao['er'])
else:
    print(situacao['a'])

