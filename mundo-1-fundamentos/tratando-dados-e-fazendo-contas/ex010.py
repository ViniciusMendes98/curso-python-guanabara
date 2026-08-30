#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5,19
real = float(input('Quantos reais você tem na carteira? R$'))
dolar = real / 5.19
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')
