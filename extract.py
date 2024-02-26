import cv2
import numpy as np
import pytesseract


def text_from_image(img):
    bytes_data = img.getvalue()
    nparr = np.fromstring(bytes_data, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Convert image gray
    gray_image = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    # extracting
    text = pytesseract.image_to_string(gray_image)
    # typewriter("Extracted text: %s" % text)
    return text

