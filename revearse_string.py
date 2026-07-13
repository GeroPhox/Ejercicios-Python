### Invertimiento de cadenas de texto sin utilizar funciones propias de Python



def chain_invertion():                       # Creamos función
    text = input("Inserte texto deseado")    # Texto a analizar
    end_of_the_text = len(text) -1           # Necesario para el range para saber el primer valor
    resultado = ""                           # Creamos variable vacía
    for i in range(end_of_the_text, -1, -1): # Creamos un for que se repetira hasta recorrer todos los elementos
        resultado = resultado + text[i]      # Cerramos la variable del resultado sumando el vació más cada letra de la cadena invertida
    return(resultado)                        # Hacemos print del resultado

print(chain_invertion())                     # Llamamos a la funcion



