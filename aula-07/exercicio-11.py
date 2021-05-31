# Você insere as medidas da parede e ele lhe passa a área da mesma e quanlos litros são necessarios para pintar a mesma
l = float(input('Largura da parede (em metros): '))
h = float(input('Altura da parede (em metros): '))
a = l*h
t = a/2
print('Sua parede tem as dimensões de {}x{} e a sua área é de {}m².'.format(l,h,a))
print('Para pintar essa parede, voĉe precisará de {:.2f2.5}l de tinta'.format(t))