import segno
import numpy as np
from PIL import Image
import streamlit as st
from app import to_bytes

st.title(" Create a QR code as you like!!!")
content = st.text_input("Enter a text you want to generate QR", placeholder="Enter text...")

if len(content) > 0:
    qr = segno.make_qr(content)
    qr.save("temp_qr.png", scale=12)
    img = Image.open("temp_qr.png")
    st.image("temp_qr.png", caption="Generated QR")
    st.download_button("Download", to_bytes(img, "png"), file_name="qr_code.png")
    st.markdown("### You can more creative your QR code")
    back = st.file_uploader("Upload image for background", type=["png", "jpg", "gif"])
    if back:
        qr.to_artistic(background=back, target='qr_with_background.png', scale=5)
        # img  = Image.open('qr_with_background.png')
        st.image('qr_with_background.png', caption="Generated QR")
 # Paste QR code onto the background at position (50,  50)
# qr.to_artistic(background='/home/holmon/Downloads/hazal.jpg', target='qr_with_background.png', scale=5)

# background = Image.open('qr_with_background.png')

