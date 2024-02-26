from rembg import remove
from PIL import Image


def removebg(file):
    img  = Image.open(file)
    rmbg = remove(img)
    return rmbg