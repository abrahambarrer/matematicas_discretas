'''
    este programa determina si un numero n es perfecto
'''

numero = int(input('Proporciona un numero: '))
divisores = []
suma = 0

for i in range(1, numero // 2 + 1):
    if numero % i == 0:
        divisores.append(i)

for i in divisores:
    suma += i

if suma == numero:
    print(True)
else:
    print(False)