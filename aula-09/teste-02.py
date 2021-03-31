# essa frase tem 21 caracteres que vão de 0 --> 20 
frase = 'Curso em video Python'
len(frase)
print(len(frase))

#conta quantas vezes aparce a caractere 0
frase.count('o')
print(frase.count('o'))

#faz uma contagem aplicando o fatiamento (nesse caso do caractere 0 até o 13)
frase.count('o',0,13)
print(frase.count('o',0,13))

#Procura uma sequancia de algarismos específicos dentro da string 
# e ele mostrara no terminal qual a posição de inicio dessas sequencia de letras 
frase.find('deo')
print(frase.find('deo'))

#quando ele procura uma coisa que não existe dentro da string ele te retorna o valor de "-1"
frase.find('android')
print(frase.find('android'))

#Procura se uma palavra existe dentro da string (Resposta será dada em "True" ou "False" verdadeiro uou falso)
'Curso' in frase
print('Curso' in frase)
