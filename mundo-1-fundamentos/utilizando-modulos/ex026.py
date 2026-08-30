#Faça um programa que leia uma frase pelo teclado e mostre:
# a) Quantas vezes aparece a letra "A"
# b) Em que posição ela aparece a primeira vez
# c) Em que posição ela aparece a última vez
frase = input('Digite uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A letra A aparece pela primeira vez na posição {frase.find('A') + 1}.')
print(f'A letra A aparece pela última vez na posição {frase.rfind('A') + 1}.')