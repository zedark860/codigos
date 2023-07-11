from math import hypot

co,ca=list(map(float, input('Digite o cateto oposto e o cateto adjacente, para saber a hipotenusa: ').split()))
h=hypot(co,ca)
print('O comprimento da hipotenusa é {:.2f}'.format(h))