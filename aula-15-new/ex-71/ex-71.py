print('-=-'*8)
print('{:^24}'.format('Banco Nacional'))
print('-=-'*8)

ValorRetirado = int(input('Qual valor vocẽ desejá sacar: R$'))

# Notas de --> 50 , 20 , 10 , 1.

cedula = 50
Total = ValorRetirado
TotalCedula = 0

while True:
    if Total >= cedula:
        Total = Total - cedula
        TotalCedula += 1
    else:
        print(f'o total de cedulas de R${cedula} foi de: {TotalCedula}')
        if cedula == 50:
            cedula = 20
            TotalCedula = 0
        elif cedula == 20:
            cedula = 10
            TotalCedula = 0
        elif cedula == 10:
            cedula = 1 
            TotalCedula = 0
        elif Total == 0:
            break
