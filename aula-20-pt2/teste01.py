#interactive help
#ajuda interativa dento do python 
#usa-se o comando help()
#help(print())


#docstring
#manual de uma função 
#começa depois do comando def,
#para usar necessita abrir aspas suplas "" 3x antes e depois da docstring
def contador(i,f,p):
    """vai contar de um numero até outro numero utilizando uma ordem
     i = valor de inicio
     f = valor de termino
     p = valor do salto"""
    
#help(contador(0,10,1))

#parametro opcional
#utilizado para caso algum valor não seja informado
def somar(a=0,b=0,c=0):
    soma = a + b + c
    print(f'A soma vale {soma}')

somar(1,2)
somar(1,2,3)

#para setar uma variavel que está dentro de uma def como global usa-se o comando global nome da variavel

#comando return 
def somar(a=0,b=0,c=0):
    soma = a + b + c
    return s
