import torch
from diffusers import StableDiffusionPipeline


image_model_id = "stabilityai/stable-diffusion-2"
device = "cuda"
image_gen_steps = 35
generator = torch.Generator(device).manual_seed(42)
guidance_scale = 9
image_size = (432, 432)
image_gen_model = StableDiffusionPipeline.from_pretrained(
    image_model_id, torch_dtype=torch.float16,
    revision="fp16" #, use_auth_token="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", guidance_scale=9
)

image_gen_model = image_gen_model.to(device)

def generate_image(prompt):
  image = image_gen_model(
      prompt, num_interface_steps=image_gen_steps,
      generator=generator, guide_scale=guidance_scale,
  ).images[0]
  image = image.resize(image_size)
  return image