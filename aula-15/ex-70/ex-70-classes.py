from operator import itemgetter 

class caixa_registradora:


    def __init__(self):
        self.total_gasto = 0
        self.produto_acima_1000 = 0
        self.produto_mais_barato = None
        self.produtos = list()
        #self.__produto_dicionario = dict()
        self.rodando = True
        self.valor_produto_mais_barato = 0

    def cadastrar_produto(self):
        nome_produto = input('Nome do Produto: ').strip()
        valor_produto = float(input('Valor: '))
        id_produto = len(self.produtos)+1
        self.produtos.append({'id':id_produto,'produto':nome_produto,'valor':valor_produto})
        

    def init_caixa_registradora(self):
        while self.rodando:
            self.cadastrar_produto()
            print(self.produtos)
            self.repetir()
        self.gerar_total_gasto()
        #print(self.total_gasto)
        self.achar_produto_acima_1000()
        #print(self.produto_acima_1000)
        self.produto_mais_barato = self.achar_produto_barato()
        #print(self.produto_mais_barato)
        self.tabela()
            

    def gerar_total_gasto(self):
        for produto in self.produtos:
            self.total_gasto += produto['valor']

    def achar_produto_acima_1000(self):
        for produto in self.produtos:
            if produto['valor'] > 1000:
                self.produto_acima_1000 += 1

    def achar_produto_barato(self):
        valores = itemgetter('valor')
        return min(self.produtos,key=valores)

    def repetir(self):
        continuar = input('Desejá continuar? [S/N] ').lower().strip()
        if continuar == 'n':
            self.rodando = False
        
    def tabela(self):
        print(f'{"-="*10}-')
        print(f'{"TABELA DE PREÇOS":^21}')
        print(f'{"-="*10}-')
        print(f'Total gasto = {self.total_gasto}')
        print(f'Produtos acima de 1000 = {self.produto_acima_1000}')
        print(f'Produto mais barato = {self.produto_mais_barato["produto"]} {self.produto_mais_barato["valor"]}')

caixa = caixa_registradora().init_caixa_registradora()