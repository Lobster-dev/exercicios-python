#funciona como um módulo pessoal
#neccesita possuir somente defs 
#facilitam a autalização dee códigos 
#modularização facilita um pouco, mas também pode ficar muito soreccaregado

def fatorial(num):
    fatorial = 1
    for c in range(1,num+1):
        fatorial*= c
        print(fatorial,end='. ')
    print('= ',end='')
    return fatorial

def dobro(num):
    multi = num*2
    return multi

def triplo(num):
    multi = num*3
    return multi