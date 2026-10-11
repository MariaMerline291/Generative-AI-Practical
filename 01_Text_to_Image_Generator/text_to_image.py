!pip install torch diffusers transformers accelerate
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import matplotlib.pyplot as plt
# Load model
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16
)
# Use GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)
# Get prompt from user
prompt = input("Enter a text prompt: ")
# Generate image
image = pipe(prompt).images[0]
# Save image
image.save("generated_image.png")
# Display image
plt.imshow(image)
plt.axis("off")  
plt.show()
print("Image saved as generated_image.png")
