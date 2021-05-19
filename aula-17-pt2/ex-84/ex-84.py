#nome e peso
Pessoas = list()

#Pessoas mais leves
PessoasLeves = list()

#Pessoas mais pesadas
PessoasPesadas = list()

#Total de pessoas cadastradas
TotalCadastrados = PesoMaior = PesoMenor = 0

#lista temporaria para armazenar os dados das pessoas
dados = list()

#Metodo 1
#Separado
while True:
    dados.append(str(input('Nome: ')).capitalize().strip())
    dados.append(int(input('Peso: ')))
    Pessoas.append(dados[:])
    TotalCadastrados += 1
    loop = input('Desejá continuar [S/N]: ').lower().strip()
    if loop == 'n':
        break
    dados.clear()
print(Pessoas)

for Nome, Peso in Pessoas:
    if Nome == Pessoas[0][0]:
        PesoMaior = Peso
        PessoasPesadas.append(Nome)
        PesoMenor = Peso
        PessoasLeves.append(Nome)
    elif Peso > PesoMaior:
        PessoasPesadas.clear()
        PessoasPesadas.append(Nome)
        PesoMaior = Peso
    elif Peso < PesoMenor:
        PessoasLeves.clear()
        PessoasLeves.append(Nome)
        PesoMenor = Peso
    elif Peso == PesoMaior:
        PessoasPesadas.append(nome)
    elif Peso == PesoMenor:
        PessoasLeves.append(nome)

print('')

print('-=-'*10)
print(f'Ao todo foram cadastradas {TotalCadastrados} pessoas')
print(f'O maior peso foi de {PesoMaior}Kg pesso de {PessoasPesadas}')
print(f'O menor peso foi de {PesoMenor}Kg pesso de {PessoasLeves} ')