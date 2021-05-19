from random import randint

# Titulo 
print('= '*15)
print('    jogo do par ou impar'.upper())
print('           v1.0')
print('= '*15)

# regras
regras = str(input('Você deseja ler as régras? [s/n] ')).lower().strip()
if regras == 's':
    print('')
    print('As regras são bem simples: ')
    print('Você escolhe se você quer pár ou impar')
    print('E depois você digita um numero')
    print('eu vou comparar o valor que você me deu, com o valor que eu pensei ')
    print('O jogo continua até você perder')
    print('Eu só vou pensar em numeros de 1 até 10')
    print('')
else: 
    print('')
    print('Então você é daqueles que não lê as regras né !!')
    print('')

input('pressione enter para jogar')

NumVit = 0

while True:

    # Escolha Par ou Impar
    print('')
    ParImpar = input('Escolha Par ou Impar: ').lower().strip()
    NumeroComputador = randint(1,10)

    #Jogo 

    if ParImpar == 'par':
        Numero = int(input('Digite o numero que você pensou: '))
        Soma = Numero + NumeroComputador
        if Soma % 2 == 0:
            NumVit = NumVit + 1
            print('Parabens!!')
            print('Você Ganhou!!')
            print(f'O numero que eu tinha pensado era: {NumeroComputador}')
            print(f'Você tem um tota de {NumVit} vitorias consecutivas')
        else:
            print('AHA eu ganhei!!')
            print(f'O numero que eu tinha pensado era: {NumeroComputador} ')
            Replay = input('Desejá jogar novamente? [S/N]').lower().strip()
            if Replay == 'n':
                break
            elif Replay == 's':
                NumVit = 0 
    elif ParImpar == 'impar':
        Numero = int(input('Digite o numero qwue você pensou: '))
        Soma = Numero + NumeroComputador
        if Soma % 2 != 0:
            NumVit = NumVit + 1
            print('Parabens!!')
            print('Você Ganhou!!')
            print(f'O numero que eu tinha pensado era: {NumeroComputador}')
            print(f'Você tem um tota de {NumVit} vitorias consecutivas')
        else:
            print('AHA eu ganhei!!')
            print(f'O numero que eu tinha pensado era: {NumeroComputador} ')
            Replay = input('Desejá jogar novamente? [S/N]').lower().strip()
            if Replay == 'n':
                break
            elif Replay == 's':
                NumVit = 0 

print(f'Você teve um total de: {NumVit} vitórias')