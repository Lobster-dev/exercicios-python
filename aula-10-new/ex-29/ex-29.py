velocidade = float(input('Qual a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('MULTADO!! Você exedeu o limite de velocidade permitido que é de 80km/h')
    print('Vocẽ deve pagar uma multa de R${}'.format(multa))
else:
    print('Você está dentro do limite de velocidade permitido')
    print('Tenha uma boa viajem!!')
