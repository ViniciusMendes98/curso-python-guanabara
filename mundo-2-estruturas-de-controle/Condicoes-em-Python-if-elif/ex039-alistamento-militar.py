#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - se ele ainda vai se alistar ao serviço militar
# - se é a hora de se alistar
# - se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade < 18:
    saldo = 18 - idade
    print(f'Você tem {idade} anos. Ainda faltam {saldo} anos para o alistamento.')
elif idade == 18:
    print(f'Você tem {idade} anos. Está na hora de se alistar!')
else:
    saldo = idade - 18
    print(f'Você tem {idade} anos. Já passou do tempo de alistamento em {saldo} anos.')