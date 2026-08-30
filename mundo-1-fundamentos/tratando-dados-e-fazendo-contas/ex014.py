#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
# A fórmula de conversão é: F = C * 9/5 + 32
c = float(input('Digite a temperatura em °C: '))
f = c * 9/5 + 32
print(f'A temperatura em °F é: {f:.1f}°F')