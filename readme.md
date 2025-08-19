# Local Chatbot with Ollama and Streamlit

This project creates a simple local chatbot web app using a local LLM model managed by [Ollama](https://ollama.com/) and a Streamlit interface.

---

## Features

- Uses a local LLM model (`llama2:latest`) through Ollama’s API
- Simple chat interface powered by Streamlit
- Fully local, no internet needed for inference
- Minimal and easy-to-understand code

---

## Setup Instructions

### 1. Install Ollama

- Download and install Ollama from [https://ollama.com/](https://ollama.com/)
- Pull the `llama2:latest` model locally by running:
```

ollama pull llama2:latest

```
- Start the Ollama API server with the model:
```

ollama run llama2:latest

```
This will start the model serving on `http://localhost:11434`.

### 2. Set up Python virtual environment

From your **project folder**, create and activate the virtual environment named `local-llm-bot-app-env`:

```

python -m venv local-llm-bot-app-env
source local-llm-bot-app-env/bin/activate   \# On Windows: local-llm-bot-app-env\Scripts\activate

```

### 3. Install Python dependencies

With the virtual environment activated, install required packages:

```

pip install streamlit requests

```

---

## Running the Chatbot App

1. Save the chatbot Python script as `app.py` inside your project folder.
2. Make sure Ollama is running with the `llama2:latest` model (see step 1).
3. From the project folder (with the `local-llm-bot-app-env` virtual environment activated), run:

```

streamlit run app.py

```

4. Open the URL shown in the terminal (default: http://localhost:8501) in your web browser.
5. Start chatting with your locally hosted LLM!

---

## How It Works

- Streamlit provides the user interface for chat input and display.
- Chat history is kept in the session state.
- The entire conversation is sent as a prompt to Ollama’s REST API locally.
- Ollama runs the `llama2:latest` model to generate replies.
- Replies are appended to the chat history and shown in the UI.

---

## Troubleshooting

- Confirm Ollama and the model server at `http://localhost:11434` are running before starting the app.
- Check your firewall/port settings if the connection to Ollama API fails.
- Ensure the virtual environment `local-llm-bot-app-env` is activated during development.

---

## License

This project is open for personal use and customization.

---


