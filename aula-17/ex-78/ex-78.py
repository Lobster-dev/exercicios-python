valores = list()
PosicaoMaior = list()
PosicaoMaior = list()



for cont in range(0,5):
    valores.append(int(input(f'Digite o vaslor da posição {cont}: ')))
    
    if cont == 0:
        maior = menor = valores[cont]
        PosicaoMaior = cont
        PosicaoMenor = cont
    else:
        if maior < valores[cont]:
            maior = valores[cont]
        if menor > valores[cont]:
            menor = valores[cont]

print('-=-'*20)
print(valores)

print(f'o maior valor digitado foi: {maior} na posições', end=' ')
for i, v in enumerate(valores):
    if  v == maior:
        print(f'{i}... ',end='')
print('')
print(f'o menor valor digitado foi: {menor} nas posições ', end=' ')
for i, v in enumerate(valores):
    if  v == menor:
        print(f'{i}... ',end='')