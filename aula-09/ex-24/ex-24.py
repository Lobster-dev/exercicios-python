cidade = input('Em que cidade você nasceu: ').strip().split()
print ('A cidade em que você nasceu começa com a palavra Santo: {}'.format('santo' in cidade[0].lower()))

# Outra maneira de digitar esse código pode ser feito dessa maneira:

# cidade = input('Em qual cidade você nasceu: ').strip().lower()
# print(cidade[:5] == 'santo')