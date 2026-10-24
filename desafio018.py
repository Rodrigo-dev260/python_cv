from math import sin, cos, tan, radians
angulo = float(input('Digite um angulo: '))
s = sin(radians(angulo))
c = cos(radians(angulo))
t = tan(radians(angulo))
print('O ânglul de {} tem o SENO de {:.2f}'.format(angulo, s))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(angulo, c))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(angulo, t))