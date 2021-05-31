# Você digita um valor e será mostrado o dobro, o triplo e a sua raiz quadrada
n = float(input('Digite um numero: '))
d = n*2
t = n*3
r = n**(1/2)
# O comando ":.2f" presente na linha 6 dentro das chaves possio a função de limitar o numero de casas flutuantes (após a virgula)
print ('O dobro de {} vale: {} \nO triplo de {} vale: {} \n A raiz de {} vale: {:.2f} '.format(n,d,n,t,n,r))