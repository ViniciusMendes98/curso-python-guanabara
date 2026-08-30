#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite o nome da pessoa: ').strip()
print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')