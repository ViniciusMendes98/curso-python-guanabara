#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome
nome = input("Digite seu nome completo: ")
print("Nome em maiúsculas:", nome.upper())
print("Nome em minúsculas:", nome.lower())
# Removendo espaços e contando letras
nome_sem_espacos = nome.replace(" ", "")
print("Quantidade de letras (sem espaços):", len(nome_sem_espacos))
# Contando letras do primeiro nome
primeiro_nome = nome.split()[0]
print("Quantidade de letras do primeiro nome:", len(primeiro_nome))
