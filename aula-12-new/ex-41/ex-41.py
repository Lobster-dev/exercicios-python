from datetime import date 

print('-=-'*10)
print('    CATEGORIAS DE NATAÇÃO')
print('-=-'*10)

Nascimento = int(input('Qual o seu ano de nascimento: '))
AnoAtual = date.today().year

idade = AnoAtual - Nascimento

if idade <= 9:
    print('A sua categoria é MIRIM!!')
elif 9 < idade <=14:
    print('A sua categoria é INFANTIL!!')
elif 14 < idade <= 19:
    print('A sua categorie é JUNIOR!!')
elif 19 < idade <= 25: 
    print('A sua categoria é SÊNIOR!!')
elif idade > 25:
    print('A sua categoria é MASTER!!')
