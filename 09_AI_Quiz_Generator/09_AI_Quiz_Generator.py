!pip install -q gradio google-generativeai
import gradio as gr
import google.generativeai as genai
API_KEY = "GEMINI_API_KEY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
def generate_quiz(topic):
    prompt = f"""
    Create a short quiz about {topic}.
Give exactly:
    3 MCQ questions with 4 options and answers.
    2 descriptive questions with short answers.
 Keep everything short.
    """
response = model.generate_content(prompt)
    return response.text
demo = gr.Interface(
    fn=generate_quiz,
    inputs=gr.Textbox(
        label="Enter Topic",
        placeholder="Example: Machine Learning"
    ),
    outputs=gr.Textbox(label="Generated Quiz", lines=20),
    title="AI Quiz Generator",
    description="Generate MCQs and descriptive questions using Generative AI."
)
demo.launch(share=True)
