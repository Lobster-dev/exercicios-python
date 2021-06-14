def Variavel_Global():
    global Texto
    Texto = 'Good morning ;)'


Texto = 'Hello World'
print (Texto)

Variavel_Global()
print(Texto)

#Adicionando o comanod "global" na def
#em vez de ser criado uma variavel local, a variavel alterada é a variavel 'Texto' que havia sido definida antes
