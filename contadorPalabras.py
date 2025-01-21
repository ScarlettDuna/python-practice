# Reto 8 de Mouredev
# Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas
# Los signos de puntuacion no forman parte de la palabra
# La palabra es la misma aunque aparezca en mayusculas y minusculas 
import re


def contador_palabras(cadena):
    cadena_limpia = re.sub(r'[^\w\s]', '', cadena.lower())
    lista = cadena_limpia.split(' ')
    # Usamos set para encontrar palabras únicas
    lista_unicas = set(lista)
    for word in lista_unicas:
        print(f'La palabra "{word}" se ha repetido {lista.count(word)} {"vez" if lista.count(word) ==1 else "veces"}.')


contador_palabras("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).")