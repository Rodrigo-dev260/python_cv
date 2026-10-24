nome = str(input('Nome Completo: '))
print('Analizando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {}'.format([0], len(separa)))

