import segno
import numpy as np
from PIL import Image
import streamlit as st


st.title(" Create a QR code as you like!!!")
content = st.text_input("Enter a text you want to generate QR", placeholder="Enter text...")

if len(content) > 0:
    qr = segno.make_qr(content)
    qr.save("temp_qr.png", scale=12)
    # img = Image.open("temp_qr.png").resize((424,424))
    # img = np.array(img)
    st.image("temp_qr.png", caption="Generated QR")
    st.download_button("Download", "temp_qr.png", file_name="qr_code.png")

 # Paste QR code onto the background at position (50,  50)
# qr.to_artistic(background='/home/holmon/Downloads/hazal.jpg', target='qr_with_background.png', scale=5)

# background = Image.open('qr_with_background.png')

