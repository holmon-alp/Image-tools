import streamlit as st
from app import to_bytes
# Uncomment the following code to use the image generator
 
import torch
from diffusers import StableDiffusionPipeline


class ImgGen:

    if torch.cuda.is_available():
        device = torch.device("cuda")
        generator = torch.Generator(device).manual_seed(42)
    else:
        device = torch.device("cpu")
        generator = torch.Generator(device).manual_seed(42)

    image_model_id = "stabilityai/stable-diffusion-2"
    # device = "cuda"

    image_gen_steps = 35
    guidance_scale = 9
    image_size = (500, 500)

    image_gen_model = StableDiffusionPipeline.from_pretrained(
        image_model_id, #torch_dtype=torch.float16,
        variant="fp16"#, use_auth_token="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", guidance_scale=9
    )

    image_gen_model = image_gen_model.to(device)

    def generate_image(prompt):
        image = ImgGen.image_gen_model(
            prompt, num_interface_steps=ImgGen.image_gen_steps,
            generator=ImgGen.generator, guide_scale=ImgGen.guidance_scale,
        ).images[0]
        image = image.resize(ImgGen.image_size)
        return image

st.set_page_config(
    page_title="Image generator",
    page_icon="💡",
)
st.title("Text to image generator")

prompt = st.text_input("Enter prompt to generate image", placeholder="Enter prompt...")
if len(prompt) > 0:
    with st.spinner('Wait a moment...'):
        img = ImgGen.generate_image(prompt)
    st.image(img)
    st.download_button(
            "Download", 
            to_bytes(img, "PNG"), 
            file_name="image.png",
            type="primary"
        )

st.warning("This feature doesn't work here because GPU doesn't support it 😥")
st.markdown(
    """
    If you want to use this feature, please follow the link below and run the program on your machine with GPU support.

    [Link](https://github.com/holmon-alp/Image-tools.git)"""
)
