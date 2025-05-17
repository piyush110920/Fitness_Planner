import streamlit as st
from app import run_chatbot_app  # Import the chatbot function
from vision import run_image_chatbot  # Import your image-to-text chatbot function
from diet_planner import diet_planner_app  # Import the diet planner function
from workout_planner import mainq    # Import the workout planner function
from PIL import Image

# Title of the web app
st.title("FitLife")

# Sidebar to choose between the four options
option = st.sidebar.selectbox(
    'Choose a solution for your healthy life',
    ('Chatbot', 'Image Descriptor', 'Diet Planner', 'Workout Planner')
)

# If the user selects Text-to-Text Chatbot
if option == 'Chatbot':
    run_chatbot_app()  # Call the chatbot app function from app.py

# If the user selects Image-to-Text Chatbot
elif option == 'Image Descriptor':
    run_image_chatbot()

# If the user selects Diet Planner
elif option == 'Diet Planner':
    st.header('Diet Planner')
    diet_planner_app()  # Call the diet planner function

# If the user selects Workout Planner
elif option == 'Workout Planner':
    st.header('Workout Planner')
    mainq()  # Call the workout planner function