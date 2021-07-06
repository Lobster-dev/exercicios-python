Nota1 = float(input('Primeira nota: '))
Nota2 = float(input('Segunda nota: '))
MediaAluno = (Nota1 + Nota2)/2
if MediaAluno >= 7:
    print('Aluno APROVADO !!')
    print(' =D')
elif 7 > MediaAluno >= 5:
    print('aluno em RECUPERAÇÃO')
elif MediaAluno < 5:
    print('Aluno REPORVADO ')
print('Sua média foi de {:.1f}'.format(MediaAluno))
