!pip install -q requests beautifulsoup4 gradio
import requests
from bs4 import BeautifulSoup
import gradio as gr
# ---------------------------------------
# Function to extract text from webpage
# ---------------------------------------
def get_webpage_text(url):
  headers = {
        "User-Agent": "Mozilla/5.0"
    }
response = requests.get(
        url,
        headers=headers,
        timeout=10
    )
soup = BeautifulSoup(response.text, "html.parser")
 # Remove unnecessary parts
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

   
 # Get paragraph text
    paragraphs = soup.find_all("p")
text = " ".join(
        p.get_text(" ", strip=True)
        for p in paragraphs
    )
return text
# ---------------------------------------
# Simple extractive summarization
# ---------------------------------------
def summarize_text(text, num_sentences=5):
# Split text into sentences
    sentences = text.split(". ")
# Select first few sentences
    summary = ". ".join(sentences[:num_sentences])
return summary
# ---------------------------------------
# Main summarization function
# ---------------------------------------
def summarize_webpage(url):
try:
 if not url:
            return "Please enter a webpage URL."
 if not url.startswith(("http://", "https://")):
            return "Please enter a valid URL."
 # Extract webpage text
        text = get_webpage_text(url)
 if len(text) < 100:
            return "Could not extract enough text from this webpage."

        # Generate summary
        summary = summarize_text(text, 5)
 return summary
except Exception as e:
 return "Error: " + str(e)
# ---------------------------------------
# Gradio Interface
# ---------------------------------------
interface = gr.Interface(
fn=summarize_webpage,
inputs=gr.Textbox(
        label="Enter Web Page URL",
        placeholder="https://example.com"
    ),
outputs=gr.Textbox(
        label="Generated Summary",
        lines=10
    ),
title="Web Page Summarizer",
description="Extracts text from a webpage and generates a simple summary."
)
# Launch application
interface.launch()
