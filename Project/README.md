# Chatbot For Image Recognition and QnA
### Prerequisites

Ensure you have the following installed:
- Python 3.9 or higher
- Virtual Environment (recommended for project isolation)

### Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/tamanna0409/chatbot.git]
   ```

2. Navigate to the cloned directory:

   ```bash
   cd ["location of the folder"]
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix or MacOS
   venv\Scripts\activate  # For Windows
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

- To run the Q&A Chatbot:

  ```bash
  streamlit run app.py
  ```

- To run the Image-to-Text Model:

  ```bash
  streamlit run vision.py
  ```