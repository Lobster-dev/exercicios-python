from random import randint
from time import sleep
from operator import itemgetter

input('pressione enter para jogar!!')

print('')

jogo = {'jogador-1': randint(1,6),'jogador-2': randint(1,6),'jogador-3': randint(1,6),'jogador-4': randint(1,6)}

ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

print('')
print(f'{"-="*13}-')
print('== RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
for indice, value in enumerate(ranking):
    print(f'{indice+1}° lugar: {value[0]} com {value[1]}')
    sleep(1)