soma = 0 
for c in range (1, 500):
    if c % 2 != 0 and c % 3 == 0:
        soma += c 
        print(c)
print(soma)
