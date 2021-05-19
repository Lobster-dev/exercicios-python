from time import sleep

def contador(inicio,fim,passo):
    for c in range(inicio,fim,passo):
        sleep(0.5)
        print(c,end="... ",flush=True)
    print()


print("a) Contando de 1 até 10")
contador(0,11,1)

print("")

print("b) De 10 até 0 de 2 em 2")
contador(10,-1,-2)

print('')

print("c) Personalizada")
inicio = int(input("Qual o valor de inicio da contagem: "))
fim = int(input("Qual o valor final da contagem: "))
passo = int(input("Qual é o passo dessa contagem: "))
contador(inicio,fim,passo)