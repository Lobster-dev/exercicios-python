from random import randint

class jogo_par_impar:

    def __init__(self):
        self.num_vit = 0
        self.estiver_rodando = True

    def init_game(self):
        self.titulo()
        self.regras()
        self.montando_jogo()

    def titulo(self):
        print('= '*15)
        print('    jogo do par ou impar'.upper())
        print('           v2.0')
        print('= '*15)

    def regras(self):
        regras = input('Você deseja ler as régras? [s/n] ').lower().strip()
        if regras == 's':
            print('')
            print('As regras são bem simples: ')
            print('Você escolhe se você quer pár ou impar')
            print('E depois você digita um numero')
            print('eu vou comparar o valor que você me deu, com o valor que eu pensei ')
            print('O jogo continua até você perder')
            print('Eu só vou pensar em numeros de 1 até 10')
            print('')
            return

        print('')
        print('Então você é daqueles que não lê as regras né !!')
        print('')

    def montando_jogo(self):
        while self.estiver_rodando:
            par_impar = input('Escolha par ou impar: ').lower().strip()
            if par_impar == 'par':
                self.criar_etapa_par()
                
            elif par_impar == 'impar':
                self.criar_etapa_impar()
            
            self.replay()
    
    def criar_etapa_par(self):
        NumeroComputador = randint(1,10)

        Numero = int(input('Digite o numero que você pensou: '))
        Soma = Numero + NumeroComputador
        if Soma % 2 == 0:
            self.num_vit += 1
            print('Parabens!!')
            print('Você Ganhou!!')
            print(f'O numero que eu tinha pensado era: {NumeroComputador}')
            print(f'Você tem um tota de {self.num_vit} vitorias consecutivas')
            return

        print('AHA eu ganhei!!')
        print(f'O numero que eu tinha pensado era: {NumeroComputador} ')
        self.num_vit = 0
    
    def criar_etapa_impar(self):
        NumeroComputador = randint(1,10)
        Numero = int(input('Digite o numero que você pensou: '))
        Soma = Numero + NumeroComputador
        if Soma % 2 != 0:
            self.num_vit += 1
            print('Parabens!!')
            print('Você Ganhou!!')
            print(f'O numero que eu tinha pensado era: {NumeroComputador}')
            print(f'Você tem um tota de {self.num_vit} vitorias consecutivas')
            return
    
        print('AHA eu ganhei!!')
        print(f'O numero que eu tinha pensado era: {NumeroComputador} ')
        self.num_vit = 0

    def replay(self):
        Replay = input('Desejá jogar novamente? [S/N]').lower().strip()
        if Replay == 'n':
            exit()

    

jogo = jogo_par_impar().init_game()