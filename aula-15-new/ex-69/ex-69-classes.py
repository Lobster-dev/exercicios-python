# ex 69 cadastro usando classes v1.3

class pessoas:

    def __init__(self):
        self.rodando = True
        #self.quantidade_homens = 0
        #self.quantidade_mulheres = 0
        #self.pessoas_maiores_18 = 0

    def init_registro(self):
        #self.titulo()
        self.informacao()
    
    def titulo(self):
        print(f"{'-='*10}-")
        print(f'{"Cadastre uma Pessoa":^21}')
        print(f"{'-='*10}-")
    
    def informacao(self):
        
        while self.rodando:
            idade = int(input('Idade: '))
            genero = input('Sexo [M/F]: ').lower().strip()
            print(genero)
            self.validacao_genero(self,genero)
            self.repeticao()
            
                
    def validacao_genero(self,genero):
        if genero == 'm':
            #self.validacao_homem()
            pass
        elif genero == 'f':
            #self.validacao_mulher(idade)
            pass
        

    #def validacao_homem(self):
    #    self.quantidade_homens += 1

    #def validacao_mulher(self, idade):
    #    if idade < 20:
    #        self.quantidade_mulheres += 1

    #def maior_idade(self, idade):
    #    if idade > 18:
    #        self.pessoas_maiores_18 += 1

    def repeticao(self):
        continuar = input('Desejá continuar: [S/N]').lower().strip()
        if continuar == 'n':
            self.rodando = False


    
cadastro = pessoas().init_registro()