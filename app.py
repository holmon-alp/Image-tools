import streamlit as st
import time
from generator import generate_image


def typewriter(text: str):
    tokens = ""
    container = st.empty()
    for i in text:
        tokens += i
        container.markdown(tokens)
        time.sleep(0.15)


st.set_page_config(
    page_title="Text to Image generator",
    page_icon="🧠",
)


st.title("Welcome to Text to Image App")

prompt = st.text_input("Enter prompt to generate image", placeholder="e.g Monkeys singing on scene")
if len(prompt) > 8:
  typewriter("Generating image for this prompt: ```%s```" % prompt)
  with st.spinner('Wait a moment...'):
    image = generate_image(prompt)
    st.image(image)
   
elif len(prompt)>0 and len(prompt)<=8:
  typewriter("Please enter more prompt")


