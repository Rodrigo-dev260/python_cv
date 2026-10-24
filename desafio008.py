valor = float(input('Digite um valor em Metros: '))
centimetro = valor * 100
milimetro = valor * 1000
print('{:.0f} mt \n{:.0f} cm\n{:.0f} mm'.format(valor, centimetro, milimetro))