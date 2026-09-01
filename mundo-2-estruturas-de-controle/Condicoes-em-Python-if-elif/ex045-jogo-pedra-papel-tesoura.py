#Crie um programa que faça o computador jogar Pedra, Papel ou Tesoura com você.
import random
opcoes = ['pedra', 'papel', 'tesoura']
jogador = input('Sua jogada (pedra/papel/tesoura): ').strip().lower()
if jogador not in opcoes:
    print('Jogada invalida.')
else:
    computador = random.choice(opcoes)
    print(f'Voce: {jogador}')
    print(f'Computador: {computador}')
    if jogador == computador:
        print('Empate')
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        print('Voce venceu')
    else:
        print('Computador venceu')