from rembg import remove
from PIL import Image

# Define the paths for the input and output images
# input_path = '/home/holmon/Downloads/Telegram Desktop/withpass.jpg'
# output_path = 'output.png'

# # Open the image
# input_img = Image.open(input_path)

# # Remove the background
# output_img = remove(input_img)

# # Save the output image
# output_img.save(output_path)

def removebg(file):
    img  = Image.open(file)
    rmbg = remove(img)
    return rmbg