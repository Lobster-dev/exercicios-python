TodosJogadores = list()
JogadorIndividual = dict()
gols = list()

while True:
    JogadorIndividual['Nome'] = input('Nome do jogador: ').strip().capitalize()
    PartidasJogadas = int(input(f'Quantas partidas {JogadorIndividual["Nome"]} jogou: '))

    TotalGols = 0

    for partidas in range (0,PartidasJogadas):
        GolsPartida = int(input(f'Quantos gols na {partidas+1}° partida: '))
        gols.append(GolsPartida)
        TotalGols += GolsPartida

    JogadorIndividual['Gols'] = gols.copy()
    JogadorIndividual['Total'] = TotalGols

    TodosJogadores.append(JogadorIndividual.copy())

    JogadorIndividual.clear()
    gols.clear()
    print('-'*35)

    loop = input('Deseja continuar[S/N]: ').lower()[0]
    if loop == "n":
        break

print('')
print(f'{"-="*17}-')
print(f'{"No":<5}{"Nome":<13}{"Gols":<10}{"Total":<5}')
print('-'*35)

for k, v in enumerate(TodosJogadores):
    print(f'{k+1:<5}',end='')
    for d in v.values():
        print(f'{str(d):<13}',end='')
    print('')

while True:
    consulta = int(input('Mostrar os dados de qual jogador (Digite 999 para parar): '))-1
    if consulta == 998:
        break
    if consulta >= len(TodosJogadores):
        print('ERRO!!Esse jogador não existe')
    else:
        print(TodosJogadores[consulta])
