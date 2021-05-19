matriz = [[0,0,0],[0,0,0],[0,0,0]]
ValoresPares = Valores3Coluna = MaiorVal2linha = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = (int(input(f'Digite um valor para a posição [{linha+1},{coluna+1}]: ')))
        if matriz[linha][coluna] % 2 == 0:
            ValoresPares += matriz[linha][coluna]
        if coluna+1 == 3 :
            Valores3Coluna += matriz[linha][coluna]
        if linha == 2 and matriz[2][coluna] > MaiorVal2linha:
            MaiorVal2linha = matriz[2][coluna]
print('-=-'*10)
print('')
for linha in range (0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('')
print('-=-'*10)

print(f'A soma dos valores pares é: {ValoresPares}')
print(f'A soma dos valores da 3° coluna é: {Valores3Coluna}')
print(f'O maior valor da 2° linha é: {MaiorVal2linha}')