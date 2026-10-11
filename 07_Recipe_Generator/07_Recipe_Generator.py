!pip install -q transformers gradio torch
import gradio as gr
from transformers import pipeline
# Load AI model
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)# Recipe Generator
def generate_recipe(ingredients):
 prompt = f"""Create a simple recipe using: {ingredients}
Recipe Name:
Ingredients:
Instructions:
"""result = generator(
        prompt,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7 )    return result[0]["generated_text"]
# Gradio Interface
app = gr.Interface(
    fn=generate_recipe,
    inputs=gr.Textbox(
        label="Enter Ingredients",
        placeholder="Example: Rice, Tomato, Onion"
    ),    outputs=gr.Textbox(label="Generated Recipe"),
    title="🍳 AI Recipe Generator",
    description="Recipe Generator using Generative AI and Prompt Engineering"
)app.launch()
