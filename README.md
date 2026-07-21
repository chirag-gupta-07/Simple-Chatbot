# Simple AI ChatBot

A beautiful, glassmorphism-styled web chat application powered by Mistral AI (via LangChain). It features dynamic AI personas (Simple, Angry, Funny, Sad) that you can toggle directly from the modern user interface.

## Features
- **Modern UI**: Sleek dark mode, glassmorphism design, and micro-animations.
- **Dynamic Personas**: Instantly switch the AI's behavior between Simple, Angry, Funny, and Sad modes.
- **FastAPI Backend**: A lightweight, fast Python backend handling routing and API requests.
- **LangChain Integration**: Connects to Mistral AI smoothly to generate responses.

## Prerequisites
- Python 3.8+
- Mistral AI API Key

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chirag-gupta-07/Simple-Chatbot.git
   cd Simple-Chatbot
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your Mistral AI API key:
   ```env
   MISTRAL_API_KEY=your_mistral_api_key_here
   ```

## Running the Application

Start the FastAPI server:
```bash
python chatbot/chatbot.py
```
*(If using a virtual environment, use `.venv\Scripts\python chatbot/chatbot.py` on Windows)*

Open your web browser and navigate to:
**http://localhost:8000**

## Technologies Used
- HTML, CSS, Vanilla JavaScript (Frontend)
- FastAPI (Backend Server)
- LangChain & Mistral AI (AI/LLM processing)
