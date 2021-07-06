import time
distancia = float(input('Qual e a distancia da sua viajem: '))
print('CALCULANDO...')
time.sleep(1)
if distancia <=200:
    valor = distancia*0.5
    print('A sua passagem ira custar R${}'.format(valor))
else:
    valor = distancia*0.45
    print('A sua passagem ira custar R${}'.format(valor))
print('Tenha uma boa viajem !!')
