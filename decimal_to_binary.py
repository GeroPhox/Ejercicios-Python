### Decimal a binario

def decimal_to_binary():  # Creamos funcion
    decimal_number = int(input("Inserte numero decimal"))  # Creamos input y lo guardamos en una variable
    reversed_binary = ""  # Creamos variable vacía

    if decimal_number == 0:
        return 0

    while decimal_number:  # Creamos loop que se cumplirá hasta que la variable sea 0
        binary_element = decimal_number % 2  # Creamos variable donde guardamos el resto y operamos
        decimal_number = decimal_number // 2  # Creamos variable donde guardamos el quociente y operamos
        reversed_binary = reversed_binary + str(binary_element)  # Vamos juntando cada resto

    end_of_the_bin = len(reversed_binary) -1  # Creamos variable para determinar hasta donde tendremos que contar
    result = ""  # Creamos variable vacía
    for i in range(end_of_the_bin, -1, -1):  # Creamos loop que se repetira por cada elemento de nuestro reversed_bin
        result = result + reversed_binary[i]  # Invertimos orden de los elementos

    return result  # Devolvemos resultado

print(decimal_to_binary())  # Hacemos print de la funcion
        

