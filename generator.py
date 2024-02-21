
import streamlit as st
import pytesseract
import cv2
import numpy as np
import urllib.request
import time

st.set_page_config(
    page_title="Text to Image generator",
    page_icon="🧠",
)


st.title("Welcome to Text to Image App")
prompt = st.text_input("Enter prompt to generate image", placeholder="e.g Monkeys singing on scene")
if len(prompt) > 8:
  typewriter("Generating image for this prompt: ```%s```" % prompt, speed)
  with st.spinner('Wait a moment...'):
    req = urllib.request.urlopen(prompt)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1)
    st.image(image)
    typewriter("Extracted text: %s" % extract_text_from_image(image))
    #image = generate_image(prompt, image_gen_model)
elif len(prompt)>0 and len(prompt)<=8:
  typewriter("Please enter more prompt")

