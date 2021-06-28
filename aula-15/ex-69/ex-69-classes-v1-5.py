#versão 1.6


class pessoas:

    def __init__(self):
        self.rodando = True
        self.quantidade_homem = 0
        self.quantidade_mulher = 0
        self.pessoas_maiores_18 = 0

    def init_registro(self):
        self.titulo()
        self.informacao()
        self.tabela_de_dados()
        
        
    def titulo(self):
        print(f"{'-='*10}-")
        print(f'{"Cadastro de Pessoa":^11}')
        print(f"{'-='*10}-")

    def informacao(self):
        while self.rodando:
            self.idade = int(input('Idade: '))
            self.genero = input('Sexo [M/F]: ').lower().strip()
            self.validacao_genero(self.genero,self.idade)
            self.repeticao()
            
    def validacao_genero(self,genero,idade):
        if genero == 'm':
            self.adiciona_quantidade_homem(idade)
            self.maiores_de_18_anos(idade)

        elif genero == 'f':
            self.adiciona_quantidade_mulher(idade)
            self.maiores_de_18_anos(idade)


    def adiciona_quantidade_homem(self,idade):
        if idade > 18:
            self.quantidade_homem += 1
        
    def adiciona_quantidade_mulher(self,idade):
        if idade < 20:
            self.quantidade_mulher += 1
    
    def maiores_de_18_anos(self, idade):
        if idade > 18:
            self.pessoas_maiores_18 += 1

    def repeticao(self):
        continuar = input('Deseja continuar [S/N]: ').lower().strip()
        if continuar == 'n':
            self.rodando = False
    

    def tabela_de_dados(self):
        print(f"{'-='*19}-")
        print(f'{"DADOS CADASTRAIS":^40}')
        print(f"{'-='*19}-")
        print(f'quantidade de homens - {self.quantidade_homem}')
        print(f'quantidade de mulheres - {self.quantidade_mulher}')
        print(f'quantidade de maiores de 18 anos - {self.pessoas_maiores_18}')
        
        

#função apresentou esse erro quando colocada pra teste
# TypeError: 'int' object is not callable

cadastro = pessoas().init_registro()

