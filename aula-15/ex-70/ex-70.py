TotalGasto = 0
# acima de R$1000
ProdutoCaro = 0
#Produto mais barato
ProdutoBarato = 0

while True: 
    NomeProduto = input('Nome do Produto: ').strip()
    ValorProduto = int(input('Valor: '))
    if TotalGasto == 0:
        ProdutoBarato = ValorProduto
        NomeProdutoBarato = NomeProduto

    elif ValorProduto < ProdutoBarato:
        NomeProdutoBarato = NomeProduto
        ProdutoBarato = ValorProduto

    if ValorProduto > 1000:
        ProdutoCaro += 1

    TotalGasto += ValorProduto

    Loop = input('Deseja continuar [S/N]: ').lower().strip()
    if Loop == 'n':
        break

NomeProdutoBarato = NomeProdutoBarato.capitalize()

print(f'O total gasto foi de: {TotalGasto} \nProdutos acima de R$1000: {ProdutoCaro} \n O produto mais barato foi: {NomeProdutoBarato} e ele curstou R${ProdutoBarato}')
