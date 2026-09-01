#Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal
num = int(input('Digite um número inteiro: '))
print(f'''Escolha a base de conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'{num} convertido para binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal é {hex(num)[2:]}')
else:
    print(f'Opção inválida!')
