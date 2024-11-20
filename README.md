# Research-Report-Chatbot

Welcome to the Research-Report-Chatbot project! This prototype chatbot leverages the power of LangChain and OpenAI's GPT models to provide information and answer queries related to the Max Planck Institute for Human Development. The chatbot is designed to interact with users through a web interface.

## Features

- **Research Report Queries**: Get insights from the MPIB research reports.
- **Website Information**: Access general information about MPIB.
- **Personnel Information**: Learn about MPIB staff members.
- **Publications**: Discover MPIB publications.
- **Organizational Structure**: Understand the organizational structure of MPIB.

## Getting Started

Follow these steps to set up and run the MPIB Chatbot on your local machine.

### Prerequisites

- Python 3.12
- Git

### Installation

1. **Clone the Repository**

   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/HannesDiemerling/Research-Report-Chatbot.git
   cd <repository-directory>
   ```
   
2. **Set Up Python Environment**

   It's recommended to use a virtual environment to manage dependencies. Run the following commands:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install Dependencies**

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

6. **Create a .env File**

   Create a .env file in the root directory of the project and add your OpenAI API key:

   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Running the Application

1. **Start the Flask Application**
   
  Run the following command to start the Flask server:
   
   ```bash
   python app.py
   ```

2. **Access the Chatbot**

  Open your web browser and go to http://127.0.0.1:5000 to interact with the chatbot.
  
### License

This project is licensed under the MIT License.
