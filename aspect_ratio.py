### Calculo del aspect ratio de una imagen a partir de un URL ###

# url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
import math
import requests

#url = input("Inserte URL")
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
url = requests.get(url)
print(url.content)

def calculate_aspect_ratio(url, height, width):
    math.gcd(height, width)