from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
#h = (co ** 2 + ca ** 2) ** (1/2)
h = hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(h))
#print('A hipotenusa vai medir: {:.2f}'.format(h))