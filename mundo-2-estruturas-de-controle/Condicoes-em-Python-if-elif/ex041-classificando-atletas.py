#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print(f'Com {idade} anos: Categoria MIRIM')
elif idade <= 14:
    print(f'Com {idade} anos: Categoria INFANTIL')
elif idade <= 19:
    print(f'Com {idade} anos: Categoria JÚNIOR')
elif idade <= 25:
    print(f'Com {idade} anos: Categoria SÊNIOR')
else:
    print(f'Com {idade} anos: Categoria MASTER')