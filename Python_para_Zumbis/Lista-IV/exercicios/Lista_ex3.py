from random import sample
vetor_1 = sample(range(100),10)
vetor_2 = sample(range(100),10)
vetor_3 = list()

for elements in zip(vetor_1, vetor_2):
    vetor_3.extend(list(elements))

print(f'v1 = {vetor_1}\nv2 = {vetor_2}\nv3 = {vetor_3} ')