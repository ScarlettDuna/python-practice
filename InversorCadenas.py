# Reto 7 de Mouredev
# Crea un programa que invierta el orden de una cadena de texto
def inversor_cadenas(cadena1):
    cadena2 = ""
    for i in range(len(cadena1)):
        cadena2 += cadena1[-i-1]
    print(cadena2)

def inversor2_cadenas(cadena1):
    print(cadena1[::-1])



inversor_cadenas("Hola mundo!")
inversor_cadenas("python")