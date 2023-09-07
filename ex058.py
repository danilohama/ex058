""" Melhore o jogo do desafio 028 onde o computador vai "Pensar" num número entre 0 e 10. Só que agora o jogador vai ten
tar adivinhar até acertar, mostrando quantos palpites foram necessários para vencer
"""
from random import randint

computador = randint(0, 10)
print('\033[33mSou seu computador...Acabei de pensar em um número entre\033[33m0 \033[36m0\033[0m e \033[36m10\033[0m')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[0mQual seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[0;31mMais... Tente mais uma vez\033[0;31m.')
        elif jogador > computador:
            print('\033[0;31mMenos... Tente mais uma vez\033[0;31m')
print('\033[32mAcertou com\033[32;0m {} \033[32mtentativas\033[32m. \033[0mParábens!'.format(palpites))
