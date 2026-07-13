### Calculo del aspect ratio de una imagen a partir de un URL ###

# url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
import math
import requests
from PIL import Image 
import io


url = input("Inserte URL")


# Ve a esa dirección y traeme lo que hay alli
response = requests.get(url)

# Sacar el contenido del url
bytes_image = response.content

# Crear un archivo que solo existe cuando se printea ya que Pillow solo abre archivos
tidied_image_bytes = io.BytesIO(bytes_image)

# Abrir el archivo
image = Image.open(tidied_image_bytes)

# Desempaquetar altura y ancho de la imagen
size = image.size
width, height = size

# Otra manera de desempaquetar la altura y el ancho de la imagen
width = size[0]
height = size[1]

# Variable que nos da el minimo comun multiplo
mcd = math.gcd(width, height)

# Funcion para obtener el aspect ratio
def calculate_aspect_ratio(width, height):
    print(width / mcd,":", height / mcd)

# Print del aspect ratio
calculate_aspect_ratio(width, height)