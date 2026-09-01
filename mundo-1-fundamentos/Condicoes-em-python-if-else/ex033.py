#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = max(n1, n2, n3)   #maximo entre os três números
menor = min(n1, n2, n3)   #mínimo entre os três números
'''Outra forma de fazer sem usar max e min:
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3'''
print(f'O maior número é {maior} e o menor número é {menor}.')