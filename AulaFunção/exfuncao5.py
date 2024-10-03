def primo(x):
    cont = 2
    while(x>2):
        div = x/cont
        cont = cont + 1
        if (x %cont==0):
            return False
        else: return True

x = int(input("Digite um número"))

print(primo(x))