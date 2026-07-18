# Contar todas las palabras de una cadena de texto sin utilizar funciones propias del programa
"""
    Crea un programa que cuente cuantas veces se repite cada palabra
    y que muestre el recuento final de todas ellas.
    - Los signos de puntuación no forman parte de la palabra.
    - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
    - No se pueden utilizar funciones propias del lenguaje que
      lo resuelvan automáticamente. """





def signs_remover():  # Creamos funcion
    word_chain = input("Inerte cadena de texto").strip().lower()  # Creamos input para recibir texto en minusculas y ignorando espacios del principio
    clean_text = ""  # Creamos variable vacía
    signs = ",.!?¡¿-_/¿¡"  # Creamos variable con los signos que no queremos
    for i in word_chain:  # Por cada elemento en esa variable...
        if i not in signs:  # Si el elemento no esta en la lista de esa variable
         clean_text = clean_text + i  # Le sumará a la variable vacía ese elemento
    return clean_text  # Devolvemos resultado

def count():  # Creamos funcion
    contador = {}  # Creamos variable vacía que será un diccionario
    final_text = signs_remover().split()  # Limpiamos el texto con las funciones
    for i in final_text:  # Por cada elemento en esa variable...
        if i not in contador:  # Si el elemento no está en el contador
            contador[i] = 1  # Ponemos el elemento con el valor 1
        else:
            contador[i] = contador[i] +1  # Sino le sumamos 1 al valor de la clave existene
    return contador  # Devolvemos resultado

print(count())  


    

        
