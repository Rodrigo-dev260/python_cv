import random
import time
from termcolor import colored
computador = random.randint(0, 5)
print(colored('=-=' * 17, 'yellow'))
print(colored('Vou pensar em número entre 0 e 5. Tente advinhar...','blue'))
print(colored('=-=' * 17, 'yellow'))
jogador = int(input('Em que número eu pennsei? '))
print('CARREGANDO...')
time.sleep(1.5) 
if jogador == computador:
    print(colored('PARABÉNS! você conseguiu vencer!','yellow'))
else:
    print(colored('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador),'red'))

