# Voce insere uma valor e ele asicionara um desconto fixticio de 5% e te passara o valor final do produto
v = float(input('Qual o valor do produto: R$'))
desc = v-(v*0.05)
print('O produto custava R${}, mas na promoção com desconto de 5% vaio custar R${:.2f}'.format(v,desc))