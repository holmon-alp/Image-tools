import streamlit as st
import time
# from generator import generate_image
import effects
import removebg
import extract
from PIL import Image
from io import BytesIO
import numpy as np



st.set_page_config(
    page_title="Image tools",
    page_icon="💡",
)


st.title("Welcome to Image tools App")


def typewriter(text: str, mark1="", mark2=""):
    tokens = ""
    container = st.empty()
    for i in text:
        tokens += i
        container.markdown(f"{mark1}{tokens}{mark2}")
        time.sleep(0.05)

def to_bytes(img, type):
    if isinstance(img, np.ndarray):
        img = Image.fromarray(img)
    img_io = BytesIO() # Buffer for save image 
    img = img.convert('RGB')
    # Save the image to the BytesIO object    
    img.save(img_io, format=type)  # Specify the format as needed
    return img_io.getvalue()

def show_and_download(image):
    
    # Display image
    st.image(image)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "Download JPEG", 
            to_bytes(image, "JPEG"), 
            file_name="image.jpg",
            type="primary"
        )
    with col2:
        st.download_button(
            "Download PNG", 
            to_bytes(image, "PNG"), 
            file_name="image.png",
            type="primary"
        )
    
    

def actions(remove, extract_t, sketch, painting, watercolor, magical, cartoonizer, classic_art, comics):
    if remove:
        with st.spinner('Wait a moment...'):
            removed = removebg.removebg(file)
            show_and_download(removed)
    if extract_t:
        with st.spinner('Wait a moment...'):
            text = extract.text_from_image(file)
            st.markdown("### Extracted text: ")
        if len(text) > 3:
            typewriter(text)
            st.info(f"{len(text)} characters")
        else: 
            typewriter("Cannot extract text from this image :(", "`", "`")
    if sketch:
        with st.spinner('Wait a moment...'):
            img  = effects.sketch(file)
            show_and_download(img)
    if painting:
        with st.spinner('Wait a moment...'):
            img = effects.painting(file)
            show_and_download(img)
    if watercolor:
        with st.spinner('Wait a moment...'):
            img = effects.watercolor(file)
            show_and_download(img)
    if magical:
        with st.spinner('Wait a moment...'):
            img = effects.magical(file)
            show_and_download(img)
    if cartoonizer:
        with st.spinner('Wait a moment...'):
            img = effects.cartoonizer(file)
            show_and_download(img)
    if classic_art:
        with st.spinner('Wait a moment...'):
            img = effects.classic_art(file)
            show_and_download(img)
    if comics:
        with st.spinner('Wait a moment...'):
            img = effects.comics(file)
            show_and_download(img)


def buttons():
    st.markdown("**Choose you want**")
    # Preparing columns for image actions
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9 = st.columns(4)
    with col1:
        remove = st.button("Remove BG", type="primary")
    with col2:
        extract_button = st.button("Extract text", type="primary")
    with col3:
        sketch =  st.button("Sketch effect", type="primary")
    with col4:
        painting = st.button("Painting effect", type="primary")
    with col5:
        watercolor = st.button("Watercolor", type="primary")
    with col6:
        magical = st.button("Magical effect", type="primary")
    with col7:
        cartoonizer = st.button("Cartoonizer effect", type="primary")
    with col8:
        classic_art = st.button("Classic art effect",  type="primary")
    with col9:
        comics = st.button("Comics effect",  type="primary")
    
    actions(
        remove, extract_button, sketch, painting, watercolor, 
        magical, cartoonizer, classic_art, comics
    )

itypes = ["png", "jpg"]

file = st.file_uploader("Upload image you want to change", type=itypes)

if file:
    typewriter("Image uploaded...", "#### ")
    st.image(file)
    buttons()
    
st.markdown(
    """
    ----
    ----
    #### This app is just an amateur creation. The app may contain errors and omissions from various situations.
    Using this program: 
    - apply effects to images;
    - remove background;
    - extract text from image;
    - generate QR code;
    - generate image via Prompt;
    
    The program was prepared by **Mirjamol Mirislomov**
    > 02.27.2024.
    
    Source code of the program on Github: [Link](https://github.com/holmon-alp/Image-tools.git)
    """
)
