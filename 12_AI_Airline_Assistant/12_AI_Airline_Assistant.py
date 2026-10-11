# Install Required Libraries

!pip install -q transformers sentencepiece accelerate gradio
import gradio as gr
# Import Libraries

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re
# Load Pre-trained Generative AI Model

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded successfully!")
# Airline Information

airline_info = """
Airline Name: SkyWays Airlines

Baggage:
Passengers can carry one cabin bag up to 7 kg.
Checked baggage allowance is up to 15 kg for economy passengers.

Check-in:
Online check-in is available 24 hours before departure.
Passengers should arrive at the airport at least 2 hours before domestic flights.

Cancellation:
Tickets can be cancelled before departure.
Cancellation charges may apply depending on the ticket type.

Flight Change:
Passengers can request a flight change before departure.
A change fee may apply depending on the ticket type.

Boarding:
Passengers should reach the boarding gate at least 30 minutes before departure.
Documents:
Passengers should carry a valid government-issued identity document for domestic travel.
Customer Support:
Passengers can contact SkyWays Airlines customer support for booking,
cancellation, refund and other travel-related queries.
"""
print("Airline Information Loaded!")
def preprocess_text(text):

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove leading and trailing spaces
    text = text.strip()

    return text
print("Preprocessing function ready!")
# Create Airline Assistant Function

def airline_assistant(user_query):

    user_query = preprocess_text(user_query)

    prompt = f"""
You are an AI Airline Assistant.
Answer the user's question using only the airline information provided below.
Give a short, clear and helpful answer.
If the information is not available, say:
"Sorry, I do not have information about that."

Airline Information:
{airline_info}
User Question:
{user_query}
Answer:
"""

    # Tokenize the prompt
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    # Generate Response
    output_ids = model.generate(
        inputs["input_ids"],
        max_length=100,
        min_length=10,
        num_beams=4,
        early_stopping=True
    )

    # Decode Response
    response = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True
    )

    return response
    # Test the AI Airline Assistant

question = "How much cabin baggage can I carry?"

answer = airline_assistant(question)

print("User Question:")
print(question)

print("\nAI Airline Assistant:")
print(answer)
interface = gr.Interface(
    fn=airline_assistant,

    inputs=gr.Textbox(
        label="Ask your Airline Question",
        placeholder="Example: How much cabin baggage can I carry?"
    ),

    outputs=gr.Textbox(
        label="AI Airline Assistant"
    ),

    title="✈️ AI Airline Assistant",

    description="Ask questions about baggage, check-in, cancellation, boarding and flight changes."
)

interface.launch()
