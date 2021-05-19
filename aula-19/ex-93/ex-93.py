AproveitamentoJogador = dict()
gols = list()

AproveitamentoJogador['Nome'] = input('Nome do jogador: ').strip().capitalize()
PartidasJogadas = int(input('Quantas partidas ele jogou: '))

TotalGols = 0

for partidas in range (0,PartidasJogadas):
    GolsPartida = int(input(f'Quantos gols na {partidas+1}° partida: '))
    gols.append(GolsPartida)
    TotalGols += GolsPartida

AproveitamentoJogador['Gols'] = gols.copy()
AproveitamentoJogador['Total'] = TotalGols

print(f'{"-="*24}-')
print(AproveitamentoJogador)
print(f'{"-="*24}-')

for Key, Value in AproveitamentoJogador.items():
    print(f'{Key} -> {Value}')

print(f'{"-="*24}-')

for c in range(0,PartidasJogadas):
    print(f'<> Na partida {c+1} o jogador fez {gols[c]} gols.')
print(f'O total de gols desse jogador foi: {TotalGols}.')