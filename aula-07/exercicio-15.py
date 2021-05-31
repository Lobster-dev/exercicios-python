# Vocẽ alugou um carro R$60.00 a diaria e por R$0.15 por km rodado
dia = float(input('Quantos dias alugados: '))
km = float(input('quantos Km percorridos: '))
d = dia*60
k = km*0.15
total = d+k 
print('O total a pagar é de: {:.2f}'.format(total))