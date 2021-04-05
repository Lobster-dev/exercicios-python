numero = int(input('Informe o numero: '))
print('Analisando o numero {}'.format(numero))
unidade = numero // 1 % 10
dezena = numero //10 % 10  
centena = numero // 100 % 10 
milhar = numero // 1000 % 10 
print('esse numero é formado por: \nUnidades: {} \nDezenas: {} \ncentenas: {} \nMilar: {} '.format(unidade,dezena, centena, milhar))
