from PIL import Image
import pillow_avif

name = "openSea_01"

img = Image.open(f'/Users/joohnny/Desktop/images/{name}.avif')
img.save(f'/Users/joohnny/Desktop/images/{name}.png')