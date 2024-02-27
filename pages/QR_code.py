import segno
from PIL import Image
import streamlit as st


st.title(" Create a QR code as you like!!!")
content = st.text_input("Enter a text you want to generate QR", placeholder="Enter text...")

if len(content) > 0:
    qr = segno.make_qr(content)
    st.image(qr)

 # Paste QR code onto the background at position (50,  50)
# qr.to_artistic(background='/home/holmon/Downloads/hazal.jpg', target='qr_with_background.png', scale=5)

# background = Image.open('qr_with_background.png')

