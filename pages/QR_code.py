import segno
from PIL import Image
import streamlit as st
from app import to_bytes, typewriter
from os import remove

# st.set_page_config(
#     page_title="QR code generator",
#     page_icon="💡",
# )


st.title(" Create a QR code as you like!!!")
content = st.text_input("Enter a text you want to generate QR", placeholder="Enter text...")
def show_(path: str, key:str):
    st.image(path, caption="Generated QR")
    img = Image.open(path)
    st.download_button("Download", to_bytes(img, "png"), file_name="qr_code.png", key=key)

if len(content) > 0:
    qr = segno.make_qr(content)
    qr.save("temp_qr.png", scale=12)
    show_("temp_qr.png", "1")

    typewriter("You can more creative your QR code", "`", "`")
    back = st.file_uploader("Upload image for background", type=["png", "jpg", "gif"])
    if back:
        qr.to_artistic(background=back, target='qr_with_background.png', scale=12)
        show_("qr_with_background.png", "2")
        remove("qr_with_background.png")
    remove("temp_qr.png")
