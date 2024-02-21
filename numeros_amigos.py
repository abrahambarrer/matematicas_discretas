'''
    este programa determina si dos numeros son amigos
'''

def amigos(numero_1, numero_2):
    divisores = []
    suma = 0

    for i in range(1, numero_1 // 2 + 1):
        if numero_1 % i == 0:
            divisores.append(i)

    for i in divisores:
        suma += i

    return True if suma == numero_2 else False

numero_1 = int(input('Proporciona numero 1: '))
numero_2 = int(input('Proporciona numero 2: '))

if amigos(numero_1, numero_2):
    print(amigos(numero_2,numero_1))
else:
    print(False)