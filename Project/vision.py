# image_chatbot.py

from dotenv import load_dotenv  # type: ignore
import os
import google.generativeai as genai  # type: ignore
import streamlit as st  # Import Streamlit
from PIL import Image  # For image processing
import pytesseract  # For OCR

# Load environment variables
load_dotenv()

# Configure API key for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate response using the Gemini model
def text_to_text_chatbot(question):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(question)
    return response.text

# Function to extract text from an image
def extract_text_from_image(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as necessary
    text = pytesseract.image_to_string(image)
    return text

def run_image_chatbot():
    st.title("Image Descriptor Chatbot")

    if "image_messages" not in st.session_state:
        st.session_state.image_messages = []

    # Upload image
    uploaded_file = st.file_uploader("Upload an image with your question", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load the image
        image = Image.open(uploaded_file)
        # Extract text from the image
        extracted_text = extract_text_from_image(image)

        if extracted_text:
            user_message = {"role": "user", "content": extracted_text}
            st.session_state.image_messages.append(user_message)
            with st.chat_message(user_message["role"]):
                st.markdown(user_message["content"])

            # Get response from Google Gemini
            response_text = text_to_text_chatbot(extracted_text)  # Call the function to get the response

            assistant_message = {"role": "assistant", "content": response_text}
            st.session_state.image_messages.append(assistant_message)
            with st.chat_message(assistant_message["role"]):
                st.markdown(assistant_message["content"])
        else:
            st.warning("No text found in the image. Please try another image.")

    # Input from the user (optional)
    if prompt := st.chat_input("What is your question?"):
        user_message = {"role": "user", "content": prompt}
        st.session_state.image_messages.append(user_message)
        with st.chat_message(user_message["role"]):
            st.markdown(user_message["content"])

        # Get response from Google Gemini
        response_text = text_to_text_chatbot(prompt)  # Call the function to get the response

        assistant_message = {"role": "assistant", "content": response_text}
        st.session_state.image_messages.append(assistant_message)
        with st.chat_message(assistant_message["role"]):
            st.markdown(assistant_message["content"])

if __name__ == "__main__":
    run_image_chatbot()