
# Fitness Planner README

## Overview
Fitness Planner is a comprehensive application designed to help users achieve their fitness goals. The application includes a chatbot for Q&A, image recognition, diet planning, and workout planning. It is deployed at [https://fitnessplanner-dxh5zbc3us2uvhtedcyztc.streamlit.app/](https://fitnessplanner-dxh5zbc3us2uvhtedcyztc.streamlit.app/).

---

## Prerequisites
- Python 3.9 or higher  
- Virtual Environment (recommended for project isolation)

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/piyush110920/Fitness_Planner.git
```

### Navigate to the Cloned Directory
```bash
cd Fitness_Planner
```

### Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Unix or MacOS
venv\Scripts\activate   # For Windows
```

### Install the Required Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Q&A Chatbot
```bash
streamlit run app.py
```

### Run the Image-to-Text Model
```bash
streamlit run vision.py
```

### Access the Diet Planning Feature
```bash
streamlit run diet_planner.py
```

### Access the Workout Planning Feature
```bash
streamlit run workout_planner.py
```

---

## Features

- **Q&A Chatbot**: A conversational AI that answers fitness-related questions.
- **Image Recognition**: A model that recognizes images of exercises and provides information about them.
- **Diet Planning**: A feature that provides personalized diet plans based on user input.
- **Workout Planning**: A feature that provides personalized workout plans based on user input.

---

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository and submit a pull request.

---


