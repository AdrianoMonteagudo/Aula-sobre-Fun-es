import math
def funcaofatorial(x):
    if x<=1:
        return 1
    else:
        return x * funcaofatorial(x-1)

x = int(input("Digite um número")) 
print(funcaofatorial(x))