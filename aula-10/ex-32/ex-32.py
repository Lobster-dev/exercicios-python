import datetime
import time 
ano = int(input('Que ano analisar? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
divisao = ano % 4
divisao2 = ano % 100
divisao3 = ano % 400
if divisao == 0 and divisao2 != 0 or divisao3 == 0:
    print('O ano {} é bissexto!!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))