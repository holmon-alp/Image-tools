import cv2
import pytesseract
import streamlit

from app import typewriter

def extract_text_from_image(img):
    # Convert image gray
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # extracting
    text = pytesseract.image_to_string(gray_image)

    return text


st.title("Extract text from image")
ftypes = ["png", "jpg"]
file = st.file_uploader("Upload image to extract text", type=ftypes)
if file:
  with st.spinner('Wait a moment...'):
    st.image(file)

  bytes_data = file.getvalue()
  nparr = np.fromstring(bytes_data, np.uint8)
  img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  typewriter("Extracted text: %s" % extract_text_from_image(img_np), speed)

