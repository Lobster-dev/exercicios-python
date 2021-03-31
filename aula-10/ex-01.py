n1 = float(input('Qual a sua 1° nota: '))
n2 = float(input('Qual a sua 2° nota: '))
media = (n1 + n2)/2
if media>=6.5:
    print('você está aprovado!!')
else:
    print('Você está de recuperação :( ')
print('Sua media foi de {}'.format(media))