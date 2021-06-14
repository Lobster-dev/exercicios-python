def par(numero):
    if numero % 2 == 0:
        return True

def divisao_por_7(numero):
    if numero % 7 == 0:
        return True


inicio = 1067
fim = 3627
numeros_possiveis = 0

for numero in range(inicio,fim+1):
    if par(numero) and divisao_por_7(numero):
        numeros_possiveis += 1

print(f'Entre {inicio} e {fim} são pares e divisiveis por 7 {numeros_possiveis} numeros')