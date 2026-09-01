#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
preco = float(input('Digite o preço do produto: R$ '))
print(f'''Escolha a condição de pagamento:
[1] - À vista dinheiro/cheque
[2] - À vista no cartão
[3] - Em até 2x no cartão
[4] - 3x ou mais no cartão''')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'Valor a ser pago: R$ {preco * 0.9:.2f}')
elif opcao == 2:
    print(f'Valor a ser pago: R$ {preco * 0.95:.2f}')
elif opcao == 3:
    print(f'Valor a ser pago: R$ {preco:.2f}')
elif opcao == 4:
    print(f'Valor a ser pago: R$ {preco * 1.2:.2f}')
else:
    print(f'Opção inválida!')