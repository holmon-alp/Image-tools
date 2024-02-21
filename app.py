import streamlit
import time


def typewriter(text: str):
    tokens = ""
    container = st.empty()
    for i in text:
        tokens += i
        container.markdown(tokens)
        time.sleep(0.15)

