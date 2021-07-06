# par ao python necessita-se que seja colocado o sinal " : " junto com o comando if, elif, e else 
tempo = int(input('Quantos anos tem o seu carro: '))
if tempo <=3:
    print('seu carro está novo')
elif 3 < tempo <=10: 
    print('Seu carro está mais gasto')
else:
    print('recomendo que você troque de carro')
print('--Thats All Folks--')

print('')

#tambem pode-se rezumir em menos linhas como no exemplo: 
tempo = int(input('Quantos anos tem o seu carro: '))
print('carro novo' if tempo<=3 else ('carro velho'))
print('--Thats All Folks--')

print('')

