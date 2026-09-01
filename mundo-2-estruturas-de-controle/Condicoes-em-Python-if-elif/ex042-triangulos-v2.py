#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais, um diferente
# Escaleno: todos os lados diferentes
r1 = float(input('Digite o comprimento do primeiro segmento: '))
r2 = float(input('Digite o comprimento do segundo segmento: '))
r3 = float(input('Digite o comprimento do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print(f'EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print(f'ESCALENO!')
    else:
        print(f'ISÓSCELES!')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo!')