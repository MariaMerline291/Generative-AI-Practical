!pip install -q transformers gradio pillow
import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
def captioner(image):
inputs = processor(
        images=image,
        return_tensors="pt"
    )
 output = model.generate(**inputs)
caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )
return caption
app = gr.Interface(
    fn=captioner,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="Image Captioning using BLIP"
)
app.launch(share=True)
