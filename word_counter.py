# Contar todas las palabras de una cadena de texto sin utilizar funciones propias del programa
"""
    Crea un programa que cuente cuantas veces se repite cada palabra
    y que muestre el recuento final de todas ellas.
    - Los signos de puntuación no forman parte de la palabra.
    - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
    - No se pueden utilizar funciones propias del lenguaje que
      lo resuelvan automáticamente. """



word_chain = input("Inerte cadena de texto").strip().lower()

def signs_remover():
    clean_text = ""
    signs = ",", "!", "¡", ".", "-", "_", "?", "¿","/"
    text_signs = ""
    for i in word_chain:
        text_signs = ""
        if i not in signs:
         clean_text = clean_text + i
    return(clean_text)

print(signs_remover())
    

        
