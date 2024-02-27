import numpy as np
import cv2
from PIL import Image, ImageEnhance, ImageFilter

impath = "/home/holmon/Downloads/Telegram Desktop/withpass.jpg"
def sketch(file):
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Invert the grayscale image
    inverted_image = 255 - gray_image
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_image, (13,13),0)
    # Invert the blurred image
    inverted_blurred = 255 - blurred_image
    # Create the pencil sketch image
    sketch_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    # Save the sketch image
    return sketch_image
    # cv2.imwrite('sketch_image.jpg', sketch_image)

# sketch(impath)

def painting(file):
    # image = cv2.imread(path)
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    # Resize the image
    image_small = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
    # Apply bilateral filter with d=15, 
    # sigmaColor=sigmaSpace=75.
    image_color = cv2.bilateralFilter(image_small, d=15, sigmaColor=75, sigmaSpace=75)
    # Upscale image to original size
    image_color = cv2.resize(image_color, (image.shape[1],image.shape[0]))
    # Convert to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply median blur
    image_gray = cv2.medianBlur(image_gray, 5)
    # Detect and enhance edges
    edges = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # Convert back to color, bit-AND with color image
    image_edge = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    image_cartoon = cv2.bitwise_and(image_color, image_edge)
    # Save the painting effect image
    return image_cartoon
    # cv2.imwrite('painting_image.jpg', image_cartoon)

# painting(impath)

def watercolor(file):
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    # Apply median blur
    image_median = cv2.medianBlur(image, 19)
    # Downscale and upscale the image to create a 'watercolor' effect
    down = cv2.pyrDown(image_median)
    up = cv2.pyrUp(down)
    # Blend the original image with the 'watercolor' image
    output = cv2.addWeighted(image, 0.5, up, 0.5, 0)
    # Save the watercolor effect image
    return output
    # cv2.imwrite('watercolor_image.jpg', output)

# watercolor(impath)

def magical(file):
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    smoothed = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
    # Convert to grayscale
    gray = cv2.cvtColor(smoothed, cv2.COLOR_BGR2GRAY)
    # Apply adaptive thresholding to create an edge mask
    edges = cv2.adaptiveThreshold(gray,  255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,  9,  9)
    # Combine the smoothed image and the edge mask
    magic = cv2.bitwise_and(smoothed, smoothed, mask=edges)
    return magic
    

# magical(impath)


def cartoonizer(file):
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply median blur to smoothen the edges
    gray = cv2.medianBlur(gray, 5)
    # Detect edges in the image
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # Apply bilateral filter to reduce the color palette of the image
    color = cv2.bilateralFilter(image, 9, 300, 300)
    # Combine the color image with the edge mask to get a cartoon-like effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    # Convert to RGB
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    # Save the cartoonized image
    return cartoon
    # cv2.imwrite('cartoon_painting.jpg', cartoon)

# cartoonizer(impath)
    

def classic_art(file):
    # Load the image
    image = Image.open(file)
    # Apply filters
    image = image.filter(ImageFilter.FIND_EDGES)
    image = image.filter(ImageFilter.SMOOTH_MORE)
    # Save the image
    return image
    # image.save('classic_art_painting.jpg')

# classic_art(impath)


def comics(file):
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply median blur to smoothen the edges
    gray = cv2.medianBlur(gray, 5)
    # Detect edges in the image
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # Convert the image to a cartoon-like image
    color = cv2.bilateralFilter(image, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    # Increase the color intensity (saturation)
    hsvImage = cv2.cvtColor(cartoon, cv2.COLOR_BGR2HSV)
    hsvImage[:,:,1] = hsvImage[:,:,1]*1.5
    cartoon = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
    # Save the cartoonized image
    return cartoon
    # cv2.imwrite('comics_boom_cartoon.jpg', cartoon)

# comics(impath)
