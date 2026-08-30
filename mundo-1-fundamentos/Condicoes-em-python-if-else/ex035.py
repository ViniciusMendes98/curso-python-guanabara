'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
Para que três retas formem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois lados.
Exemplo:
Digite o comprimento da primeira reta: 5
Digite o comprimento da segunda reta: 7
Digite o comprimento da terceira reta: 10
As retas podem formar um triângulo.
Digite o comprimento da primeira reta: 1
Digite o comprimento da segunda reta: 2
Digite o comprimento da terceira reta: 3
As retas não podem formar um triângulo.'''

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')