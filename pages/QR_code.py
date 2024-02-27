import segno
import numpy as np
from PIL import Image
import streamlit as st
from app import to_bytes

st.title(" Create a QR code as you like!!!")
content = st.text_input("Enter a text you want to generate QR", placeholder="Enter text...")
def show_(path: str):
    st.image(path, caption="Generated QR")
    img = Image.open(path)
    st.download_button("Download", to_bytes(img, "png"), file_name="qr_code.png")

if len(content) > 0:
    qr = segno.make_qr(content)
    qr.save("temp_qr.png", scale=12)
    show_("temp_qr.png")

    st.markdown("### You can more creative your QR code")
    back = st.file_uploader("Upload image for background", type=["png", "jpg", "gif"])
    if back:
        qr.to_artistic(background=back, target='qr_with_background.png', scale=12)
        show_("qr_with_background.png")
 