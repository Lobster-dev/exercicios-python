frase = input('Digit uma frase: ').strip().lower()
print ('A letra a aparece {} vezes nessa frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição: {}'.format(frase.find('a')+1))
print('A ultima letra A apareceu na posição: {}'.format(frase.rfind('a')))
