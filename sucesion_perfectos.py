'''
    este programa calcula los numeros perfectos hasta un numero n
'''

def perfecto(numero):
    divisores = []
    suma = 0

    for i in range(1, numero // 2 + 1):
        if numero % i == 0:
            divisores.append(i)

    for i in divisores:
        suma += i

    if suma == numero:
        print(numero)

numero = int(input('Proporciona numero: '))

for i in range(2, numero + 1):
    perfecto(i)