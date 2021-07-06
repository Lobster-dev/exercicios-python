print('-=-'*12)
print('   ANALISADOR DDE TRIANGULOS')
print('-=-'*12)
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1+l2>l3 and l2+l3>l1 and l1+l3>l2:
    print ('Os segmentos acima podem formar um triangulo!!')
else :
    print('Os segmentos acima não podem formar um triangulo!!')