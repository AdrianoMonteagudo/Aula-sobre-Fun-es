import math
def funcao(a, b, c):

    x1 = (-b+(b**2-4*a*c)**0.5)/2*a
    x2 = (-b-(b**2-4*a*c)**0.5)/2*a

    return (x1, x2)

a = int(input("O valor de a"))
b = int(input("O valor de b"))
c = int(input("O valor de c"))

print(funcao(a, b, c))