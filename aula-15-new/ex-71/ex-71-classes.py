class caixa_eletronico:

    def __init__(self):
        self.rodando = True
        self.cedulas = [50,20,10,1]
        self.contador = 0
        self.total_cedulas = 0
        

    def init_caixa_eletronico(self):
        self.titulo()
        self.valor_a_retirar = int(input('Desejá retirar quantos reais: R$'))
        self.total = self.valor_a_retirar

        while self.rodando:
            self.calculador_de_cedulas()
            if self.contador == len(self.cedulas):
                self.rodando = False


    def titulo(self):
        print('-=-'*8)
        print(f'{"Banco Nacional":^24}')
        print('-=-'*8)

    def calculador_de_cedulas(self):
        if self.total >= self.cedulas[self.contador]:
            self.total -= self.cedulas[self.contador]
            self.total_cedulas += 1

        elif self.total < self.cedulas[self.contador]:
            print(f'o total de cedulas de R${self.cedulas[self.contador]} foi de: {self.total_cedulas}')
            self.total_cedulas = 0
            self.contador += 1


caixa = caixa_eletronico().init_caixa_eletronico()