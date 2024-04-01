import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def load_model():
    tokenizer = AutoTokenizer.from_pretrained("2003achu/stressed_or_notstressed_10")
    model = AutoModelForSequenceClassification.from_pretrained("2003achu/stressed_or_notstressed_10")
    return tokenizer, model

def predict_stress(text, tokenizer, model):
    # Encode the text
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    # Get predictions
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predictions = predictions.cpu().detach().numpy()
    # Convert the prediction to a binary label
    if predictions[0][1] > predictions[0][0]:
        return "Not stressed"
    else:
        return "Stressed"

# Sidebar
st.sidebar.title("About Project")
st.sidebar.write(
    "This is a simple Streamlit application that predicts whether the input text indicates stress or not. "
    "It uses a pre-trained text classification model to make predictions."
)

# Footer

# Main content
st.title("Stress Detector")

# Load model
tokenizer, model = load_model()

# Input text
input_text = st.text_input("Enter your text:")

# Predict stress level
if st.button("Predict"):
    if input_text:
        with st.spinner('Predicting...'):
            score = predict_stress(input_text, tokenizer, model)
        st.write(f"Prediction: {score}")
    else:
        st.write("Please enter some text.")


st.markdown("---")