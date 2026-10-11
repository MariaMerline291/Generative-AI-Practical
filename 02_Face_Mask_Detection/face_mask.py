!pip install transformers torch pillow gradio
import gradio as gr
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
# Load model
model_name = "DamarJati/Face-Mask-Detection"
model = AutoModelForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)
# Labels
id2label = {
    0: "Mask Found",
    1: "Mask Not Found"
}
def detect_face_mask(image):
    image = Image.fromarray(image).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        prediction_idx = torch.argmax(logits, dim=1).item()
 return id2label[prediction_idx]
iface = gr.Interface(
    fn=detect_face_mask,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Text(label="Mask Status"),
    title="Face Mask Detection",
    description="Upload an image to check whether a face mask is present."
)
iface.launch(share=True)
