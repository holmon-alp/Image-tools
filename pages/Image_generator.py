import streamlit as st
"""
 Uncomment the following code to use the image generator
"""
# import torch
# from diffusers import StableDiffusionPipeline

# image_model_id = "stabilityai/stable-diffusion-2"
# # device = "cuda"
# device = torch.device("cuda")
# image_gen_steps = 35
# generator = torch.Generator(device).manual_seed(42)
# guidance_scale = 9
# image_size = (432, 432)

# image_gen_model = StableDiffusionPipeline.from_pretrained(
#     image_model_id, torch_dtype=torch.float16,
#     variant="fp16" #, use_auth_token="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", guidance_scale=9
# )

# image_gen_model = image_gen_model.to(device)

# def generate_image(prompt):
#   image = image_gen_model(
#       prompt, num_interface_steps=image_gen_steps,
#       generator=generator, guide_scale=guidance_scale,
#   ).images[0]
#   image = image.resize(image_size)
#   return image

# st.set_page_config(
#     page_title="Image generator",
#     page_icon="💡",
# )
# st.title("Text to image generator")

# prompt = st.text_input("Enter prompt to generate image", placeholder="Enter prompt...")
# if len(prompt) > 0:
#     with st.spinner('Wait a moment...'):
#         img = generate_image(prompt)
#     st.image(img)
#     st.download_button(
#             "Download", 
#             to_bytes(img, "PNG"), 
#             file_name="image.png",
#             type="primary"
#         )

st.warning("This feature doesn't work here because GPU doesn't support it 😥")
st.markdown(
    """
    If you want to use this feature, please follow the link below and run the program on your machine with GPU support.

    [Link](https://github.com/holmon-alp/Image-tools.git)"""
)
