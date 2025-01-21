# Reto 4 de Mouredev
#Escribe un programa que se encargue de comprobar si un numero es primo o no
def esPrimo(num):
    if num <= 0:
        return False
    # para ser mas eficiente, iteramos solo hasta la raiz cuadrada de num 
    for i in range(2, int(num**0.5)+ 1):
        if (num % i == 0): 
            return False
    return True

print(esPrimo(-17))