#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário: R$ '))
anos = int(input('Anos para pagar: '))
prestacao = casa / (anos * 12)
minimo = salario * 0.3
if prestacao <= minimo:
    print(f'Aprovado! Prestação: R$ {prestacao:.2f}')
else:
    print(f'Negado! Prestação: R$ {prestacao:.2f}')