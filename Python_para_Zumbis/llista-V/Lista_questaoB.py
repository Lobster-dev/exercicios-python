quantidade_oi = 0
for i in range(1,10):
    if i != 3:
        for j in range(1,7):
            print('Oi',end=' ')
            quantidade_oi += 1 
print()
print(f'Foram escritas {quantidade_oi} vezes a palavra "Oi"')