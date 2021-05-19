from random import randint
from time import sleep

# titulo
print('-=-'*10)
print('     JOGUINHO DOS NUMEROS')
print('           PARTE 1')
print('-=-'*10)
print('Eu estou pensando em um número de 1 a 10')
print('Será que você pode adivinhar qual é esse numero? ')

# regras
regras = str(input('Você deseja ler as régras? [S/N] ')).lower().strip()
if regras == 's':
    print('')
    print('As regras são bem simples: ')
    sleep(0.5)
    print('Você terá infinitas tentativas')
    sleep(0.5)
    print('em cada tentativa você falará um numero e eu lhe direi se ele está certo ou errado')
    sleep(0.5)
    print('Em quantas tentativas será que você consegue adivinhar ?? ')
else: 
    print('')
    print('Então você é daqueles que não lê as regras né !!')
    print('')

sleep(0.5)
print('Boa sorte !!')

input('Pressione enters para jogar !!')
print('')

# Gerando um número automatico !!
NumeroAleatorio = randint(1,10)
print('Gerando número ... ')
sleep(0.5)

# Jogo
Resposta = 0
Tentativas = 0
while Resposta != NumeroAleatorio:
    Resposta = int(input('Em qual número eu pensei? '))
    print('')
    Tentativas = Tentativas + 1
print('PARABENS!!')
print('Você acertou em {} tentativas'.format(Tentativas))


