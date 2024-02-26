import streamlit as st
import time
# from generator import generate_image
import convert
import effects
import removebg
import extract 

st.set_page_config(
    page_title="Image tools",
    page_icon="🧠",
)


st.title("Welcome to Image tools App")


def typewriter(text: str, mark1="", mark2=""):
    tokens = ""
    container = st.empty()
    for i in text:
        tokens += i
        container.markdown(str(mark1)+tokens+str(mark2))
        time.sleep(0.05)

def actions(remove, extract, sketch, painting, watercolor, magical, cartoonizer, classic_art, comics):
    if remove:
        removed = removebg.removebg(file)
        st.image(removed)
    if extract:
        text = extract.text_from_image(file)
        typewriter(text, "```", "```")
    if sketch:
        img  = effects.sketch(file)
        st.image(img)
    if painting:
        img = effects.painting(file)
        st.image(img)
    if watercolor:
        img = effects.watercolor(file)
        st.image(img)
    if magical:
        img = effects.magical(file)
        st.image(img)
    if cartoonizer:
        img = effects.cartoonizer(file)
        st.image(img)
    if classic_art:
        img = effects.classic_art(file)
        st.image(img)
    if comics:
        img = effects.comics(file)
        st.image(img)


itypes = ["png", "jpg"]

file = st.file_uploader("Upload image", type=itypes)
if file:
    typewriter("Image uploaded...", "####")
    st.image(file)
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










# prompt = st.text_input("Enter prompt to generate image", placeholder="e.g Monkeys singing on scene")
# if len(prompt) > 8:
#   typewriter("Generating image for this prompt: ```%s```" % prompt)
#   with st.spinner('Wait a moment...'):
#     image = generate_image(prompt)
#     st.image(image)
   
# elif len(prompt)>0 and len(prompt)<=8:
#   typewriter("Please enter more prompt")


