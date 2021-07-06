from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
#computador gera um numero
numero = randint(1,5)
# Jogador responde
resposta = int(input('Em que nuemro eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if numero==resposta:
    print('PARABENS!! Você conseguiu me vencer :) ')
else :
    print('GANHEI!! Eu pensei no numero {} e não {}'.format(numero,resposta))
