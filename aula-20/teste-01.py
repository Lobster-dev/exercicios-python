#Rotina 
#Funções

#para criar uma função usa-se o comando: 
#def NomeDaFunção():
#    o que a função irá desempenhar
#Todas as funções do python usam parenteses depois do nome

#também é possivel fazer isso com parametros 
#ou sejá fazer um comado que se adapte utilizando parametros

#nesse caso abaixo o parametro que está dentro do parenteses equivale a mensagem que irá no meio da def
def message(msg):
    print(f"{'-='*10}-")
    print(f'{msg:^21}')
    print(f"{'-='*10}-")

message('Olá mundo')
message('Olá mundo'.upper())

def soma(a,b):
    print(f'a = {a} b = {b}')
    s = a + b
    print(f'A soma de a + b vale: {s}')

soma(5,3)



#Empacotamento de parametros
# o simbolo  " * " segnifica desempacotar
# ou sejá nesse caso abaixo independentemente da quantidade de valores passados eles serão jogados pra " num " 
def contador(*num):
    print(num)
    for valor in num:
        print(f'{valor}',end="...")
    print()

contador(0, 3, 4)
contador(1, 2, 3, 4, 5, 6)
contador(0, 1)

valores = [1,2,3,4,5,6]

def dobra(value):
    print(value)
    pos = 0
    while pos<len(value):
        value[pos] *= 2
        pos += 1
    print(value)

dobra(valores)

def soma(*num):
    print(num)
    s = 0
    for valores in num:
        s += valores 
    print(f'A soma dos valores digitados foi: {s}')

soma(1,2,3,4,5,6,7,8,9,10)



