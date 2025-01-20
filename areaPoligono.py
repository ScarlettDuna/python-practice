# Reto 5 de mouredev
# Escribe una unica funcion que sea capaz de calcular y retornar el area de un poligono.
def area_poligono(alt, ancho, poligono):
    if (ancho <= 0 or alt <= 0 ):
        return "Datos incorrectos, los datos tienen que ser positivos"
    if poligono == 4:
        return alt * ancho
    elif poligono == 3:
        return (alt * ancho) / 2
    else:
        return "Error: polígono no soportado"
    
print(area_poligono(4, 5, 4))
print(area_poligono(4, 5, 3))
print(area_poligono(4, 5, 5))
print(area_poligono(4, 5, 6))
