# você da um valor em graus celcius (°C) e ele lhe dara um resultado equivalente em Fahrenheit
c = float(input('A temperatura em °C: '))
f = (c*9/5)+32
print('A temperatura de {}°C correspondea {:.3f}°F'.format(c,f))