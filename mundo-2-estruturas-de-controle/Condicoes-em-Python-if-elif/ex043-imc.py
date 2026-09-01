#Desenvolva uma lógica para calcular o IMC (Índice de Massa Corporal) e classificar o resultado
peso = float(input('Digite o peso (kg): '))
altura = float(input('Digite a altura (m): '))
imc = peso / (altura ** 2)
print(f'O IMC é {imc:.2f}')
if imc <= 18.5:
    print(f'Classificação: Abaixo do peso')
elif imc <= 24.9:
    print(f'Classificação: Peso ideal')
elif imc <= 29.9:
    print(f'Classificação: Sobrepeso')
elif imc <= 34.9:
    print(f'Classificação: Obesidade grau I')
elif imc <= 39.9:
    print(f'Classificação: Obesidade grau II')
else:
    print(f'Classificação: Obesidade grau III (mórbida)')