# Conversor de medidas
# Vocẽ digita um valor em m e ele convertera o mesmo pra Km, hm, dam, dm, ca e mm
m = float(input('Uma distancia em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('A medida de {}m corresponde a: \n{}Km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(m,km,hm,dam,dm,cm,mm))