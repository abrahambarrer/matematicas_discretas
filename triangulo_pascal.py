'''
    este programa muestra las n + 1 filas del
    triangulo de Pascal
'''

def combinacion(n):
    x = 1
    r = 1
    print(1, end=' ')
    for i in range(n, 0, -1):
        x *= i
        r *= n - i + 1
        print(x // r, end=' ')

for i in range(0, int(input('Proporciona n: ')) + 1):
    combinacion(i)
    print()