!pip uninstall -y torch torchvision torchaudio
!pip install -q torch torchvision torchaudio
!pip install -q transformers sentencepiece accelerate
import torch
print(torch.__version__)
from transformers import BartTokenizer, BartForConditionalGeneration
import re
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)
print("Model loaded successfully!")
def preprocess_text(text):
# Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
# Remove leading/trailing spaces
    text = text.strip()
return text
    document = """
Artificial Intelligence (AI) is rapidly transforming industries worldwide.
It is used in healthcare for disease prediction and diagnosis, in finance
for fraud detection, and in education for personalized learning.
Machine learning and deep learning enable systems to learn from large
amounts of data and make intelligent decisions.
Organizations use AI to automate repetitive tasks, improve productivity,
and enhance customer experiences. As technology advances, AI is expected
to play a critical role in solving complex problems and driving innovation.
"""document = document * 20
document = preprocess_text(document)
print("Preprocessing Completed")
inputs = tokenizer(
    document,
    max_length=1024,
    truncation=True,
    return_tensors="pt"
)print("Document Tokenized Successfully!")
summary_ids = model.generate(
    inputs["input_ids"],
    max_length=100,
    min_length=30,
    num_beams=4,
    early_stopping=True
)summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)print("Generated Summary:")
print(summary)
def split_text(text, chunk_size=500):
 words = text.split()
chunks = []
 for i in range(0, len(words), chunk_size):
 chunk = " ".join(words[i:i + chunk_size])
chunks.append(chunk)
return chunks
def summarize_large_document(text):
  chunks = split_text(text)
summaries = []
for chunk in chunks:
 inputs = tokenizer(
            chunk,
            return_tensors="pt",
            max_length=1024,
            truncation=True
        )summary_ids = model.generate(
            inputs["input_ids"],
            max_length=80,
            min_length=20,
            num_beams=4
        )summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )summaries.append(summary)
  final_summary = " ".join(summaries)
 return final_summary
    final_summary = summarize_large_document(document)
print("Final Summary:\n")
print(final_summary)
