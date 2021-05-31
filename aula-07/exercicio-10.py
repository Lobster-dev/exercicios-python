# você digita uma quantia e ele te responde quantos dolat=res voê pode comprar com essa quantia 
# valor base do dolar: R$5.49
r = float(input('Digite um valor em Reais: '))
valor = r/5.49
print("Com R${} você pode adiquirir US${:.2f}".format(r,valor))