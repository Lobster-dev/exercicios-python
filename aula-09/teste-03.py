frase = 'Curso em vídeo Python'
# escreve o caractere 9 da função "Frase"
print (frase[9])

print('')

# escreve dos caracteres 9 a 14 na função
print (frase[9:14])

print('')

#escreve do caractere 0 até o 5 na função
print(frase[:5])

print('')

#escreve do caractere 15 até o final fa função
print(frase[15:])

print('')

#escreve toda a string oulando de 2 em 2 espaços
print(frase[::2])

print('')

#escreve do caractere 9 até o final pulando de 3 em 3 caracteres
print(frase[9::3])

print('')

# essa frase tem 21 caracteres que vão de 0 --> 20 
len(frase)
print(len(frase))

#conta quantas vezes aparce a caractere 0
frase.count('o')
print(frase.count('o'))

print('')

#faz uma contagem aplicando o fatiamento (nesse caso do caractere 0 até o 13)
frase.count('o',0,13)
print(frase.count('o',0,13))

print('')

#Procura uma sequancia de algarismos específicos dentro da string 
# e ele mostrara no terminal qual a posição de inicio dessas sequencia de letras 
frase.find('deo')
print(frase.find('deo'))

print('')

#quando ele procura uma coisa que não existe dentro da string ele te retorna o valor de "-1"
frase.find('android')
print(frase.find('android'))

print('')

#Procura se uma palavra existe dentro da string (Resposta será dada em "True" ou "False" verdadeiro uou falso)
'Curso' in frase
print('Curso' in frase)

print('')

# Troca a palavra uma palavra por outra (Nesse caso ele troca a palavra "Python" pela palavra "Android")
frase.replace('Python','Android')
print(frase.replace('Python','Android'))

print('')

#Deixa a string com seus algaritimos todos em maiusculo
frase.upper()
print(frase.upper())

print('')

#Deixa a string com seus algaritimos todos em minusculo
frase.lower()
print(frase.lower())

print('')

#Deixa a frase Captalizada (Deixa todos os algarismos em minusculo, com execção  da 1° lettra da string)
frase.capitalize()
print(frase.capitalize())

print('')

# analisa todas as palavras e deixa cada uma das palavras Captalizadas
frase.title()
print(frase.title())

print('')

frase1 = '   Aprenda Python  '

# Remove todos os espaços INUTEIS (do inicio e do final) da sua string espaços entre paravras NÃO sao removidos
frase1.strip()
print(frase1.strip())

print('')

#Variações do comando .strip()
# Remove somente os espaços INUTEIS  do lado DIREITO da sua string
frase1.rstrip()
print(frase1.rstrip())

print('')

# Remove somente os espaços INUTEIS  do lado ESQUERDA da sua string
frase1.lstrip()
print(frase1.lstrip())

print('')

# Funcionalidades de Divisão

# Gera uma lista com todas as palavras de uma cadeia de caracteres 
# ex: na frase Curso em video python 
# que é formada por 21 caracteres  (de 0 => 20)
# ele dividira em  4 palavras com mumerações começando em 0 no começo de cara palavra e colocara essas palavras dentro de um outro bloco 
# que fara com que ao invez de cada caractere receber uma numeração cada palavra recebera um valor 
frase.split()
print(frase.split())

print('')

# é o contrario ao .split() que ao invez de separar junta as palavras (porem nesse caso ele coloca um - ao invez de espaços)
'-'.join(frase)
FraseSplitada = frase.split()
print('-'.join(FraseSplitada))

print('')

# Tambem pode-se utilizar comandos em conjunto como:
print(frase.upper().count('O'))
# nesse caso ele jogará todas as letras em maiusculo (.upper()) e depois contara (.count()) quantas letras "O" existem nessa frase.

print('')

#tamvém pode-se alterar partes de uma string com o comando .replace() e depois salvalas 
# COmo por exemploi:
frase3 = 'Curso em Vídeo Python'
print(frase3)
frase3 = frase.replace('Python', 'Android')
print(frase3)

print('')

# Com o comando .plit você transfroma uma Frase (str) em uma pequena lista, porem você pode escrever cada elemento da lista como:
Lista = frase.split()
print(Lista[0])

print('')

# Você tambem pode pedir para que ele mostre um algarism oespecifico dentro de uma palavra de uma lista como:
print(Lista[2] [3])
# Nesse caso você pediu para que ele mostrasse o 3 algarismo do 2 item da lista 
# 2° item da lista['Vídeo'] e o seu 3° algarismo é a letra ['e']

print('')