#Escreva um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o salário do funcionário: R$ '))

if salario > 1250:
    novo_salario = salario + (salario * 0.10)
    print(f'O novo salário será de R$ {novo_salario:.2f}')
else:
    novo_salario = salario + (salario * 0.15)
    print(f'O novo salário será de R$ {novo_salario:.2f}')