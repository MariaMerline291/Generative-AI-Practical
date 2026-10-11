!pip install -q google-generativeai gradio pillow
import google.generativeai as genai
import gradio as gr
from PIL import Image
# Configure Gemini API
genai.configure(api_key="GEMINI_API_KEY")
# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")
# Function
def multimodal_assistant(image, question):
 image = Image.open(image)
 response = model.generate_content(
        [question, image]
    )
return response.text
# Gradio Interface
app = gr.Interface(
    fn=multimodal_assistant,
    inputs=[
        gr.Image(type="filepath", label="Upload Image"),
        gr.Textbox(label="Ask a Question")
    ],
    outputs=gr.Textbox(label="AI Response"),
    title="Multimodal AI Assistant using Gemini",
    description="Upload an image and ask questions about it."
)
app.launch(share=True, debug=True)
