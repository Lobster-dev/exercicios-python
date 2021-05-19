pessoa = {'nome': 'gutavo','sexo': 'm', 'idade':22 }
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(f'o {pessoa["nome"]} tem {pessoa["idade"]} anos')

print('')

print(pessoa.values())
print(pessoa.keys())
print(pessoa.items())

print('')

for key in pessoa.keys():
    print(key)

for key, value in pessoa.items():
    print(f'{key} = {value}')