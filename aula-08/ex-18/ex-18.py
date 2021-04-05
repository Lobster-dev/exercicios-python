from math import sin, cos, tan, pi
ang = float(input('Digite o angulo que você deseja: '))
rad = ang*(pi/180)
sen = sin(rad) 
cos = cos(rad)
tag = tan(rad)

print('O ângulo de {} tem o SENO de {:.3f}'.format(ang, sen))
print('O ângulo de {} tem o COSSENO de {:.3f}'.format(ang, cos))
print('O ângulo de {} tem a TANGENTE de {:.3f}'.format(ang, tag))
