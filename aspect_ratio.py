### Calculo del aspect ratio de una imagen a partir de un URL ###

# url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
import math
import requests
from PIL import Image 
import io


#url = input("Inserte URL")
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
response = requests.get(url)
undefined_image = response.content
image = io.BytesIO(undefined_image)
print(open(image))



def calculate_aspect_ratio(response, height, width):
    math.gcd(height, width)