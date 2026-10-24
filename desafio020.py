from random import shuffle
a1 = input('Digite o primeiro aluno: ')
a2 = input('Digite o segundo aluno: ')
a3 = input('Digite o terçeiro aluno: ')
a4 = input('Digite o quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('Os alunos sorteados foram:')
print(lista)

