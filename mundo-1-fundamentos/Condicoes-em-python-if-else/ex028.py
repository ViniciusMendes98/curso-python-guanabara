#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
numero_computador = random.randint(0, 5)
numero_usuario = int(input('Tente adivinhar o número que o computador pensou (entre 0 e 5): '))
if numero_usuario == numero_computador:
    print(f'Parabéns! Você acertou!')
else:
    print(f'Que pena! O número correto era {numero_computador}.')