!pip install -q -U transformers accelerate gradio
import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
# Name of the pretrained coding model
model_name = "Qwen/Qwen2.5-Coder-0.5B-Instruct"
# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
# Load model
model = AutoModelForCausalLM.from_pretrained(model_name)
print("Code AI Model Loaded Successfully!")
def generate_code(prompt):
# Create an instruction for the AI model
instruction = f"""You are a Python code generator.
Generate correct Python code for the following requirement.
Requirement:
{prompt}
Rules:
1. Generate only Python code.
2. Do not include explanations.
3. Do not include markdown code fences.
4. Write simple and readable code.
5. Add comments where useful.
Python code:
"""
# Convert prompt into tokens
 inputs = tokenizer(
        instruction,
        return_tensors="pt"
    )
 # Generate code
with torch.no_grad():
  outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.2,
            top_p=0.9
        )
# Convert generated tokens back to text
generated_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )
# Remove the original instruction
 generated_code = generated_text[len(instruction):].strip()
return generated_code
    # Test the AI code generator
prompt = "Write a Python program to find the factorial of a number."
result = generate_code(prompt)
print(result)
# Create Gradio interface

demo = gr.Interface(
    fn=generate_code,
 inputs=gr.Textbox(
        lines=5,
        placeholder="Enter your Python programming requirement...",
        label="Python Programming Requirement"
    ),
outputs=gr.Code(
        language="python",
        label="Generated Python Code"
    ),
 title="AI Python Code Generator",
 description="Generate Python code using a code-specific AI model.",
 examples=[
        ["Write a Python program to find the factorial of a number."],
        ["Write a Python program to check whether a number is prime."],
        ["Write a Python program to calculate the average of three numbers."],
        ["Write a Python program to sort a list of numbers."]
    ]
)
demo.launch(share=True)
