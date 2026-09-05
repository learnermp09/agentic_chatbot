
```
# Agentic AI Chatbot

A simple AI chatbot built with Python, Streamlit, FastAPI, LangChain, and Groq.

The project follows a separate frontend and backend architecture. Streamlit provides the chat interface, while FastAPI exposes the API used to communicate with the LangChain-based chatbot.

---

## Project Structure

```text
agentic_chatbot/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   └── chatbot.py
│
├── frontend/
│   ├── app.py
│   └── decodix_logo.png
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE

```

---

## Architecture

```
User
 │
 ▼
Streamlit Frontend
   app.py
 │
 │ POST /chat
 ▼
FastAPI Backend
   main.py
 │
 ▼
Chatbot
   chatbot.py
 │
 ▼
LangChain
 │
 ▼
Groq LLM

```

---

## Technologies Used

* **Python**
* **Streamlit**
* **FastAPI**
* **LangChain**
* **Groq**
* **Uvicorn**
* **Git & GitHub**

---

## Setup

### 1. Clone the repository

```cmd
git clone [https://github.com/your-username/agentic_chatbot.git](https://github.com/your-username/agentic_chatbot.git)
cd agentic_chatbot

```

### 2. Create and activate the environment

```cmd
conda create -n ai python=3.11 -y
conda activate ai

```

### 3. Install dependencies

```cmd
pip install -r requirements.txt

```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Chatbot with search

```

> **Note:** Do not commit `.env` or API keys to GitHub.

Make sure `.gitignore` contains:

```text
.env
__pycache__/
*.pyc
.venv/

```

---

## Running the Application

The backend and frontend run separately.

### 1. Start the FastAPI Backend

From the project root:

```cmd
uvicorn backend.main:app --reload

```

* **API Base URL:** `http://127.0.0.1:8000`
* **Interactive API Docs (Swagger UI):** `http://127.0.0.1:8000/docs`

### 2. Start the Streamlit Frontend

Open another terminal:

```cmd
conda activate ai
cd agentic_chatbot
streamlit run frontend/app.py

```

* **Streamlit Web App:** `http://localhost:8501`

---

## API Documentation

### Health Check

* **Endpoint:** `GET /health`
* **Response:**
```json
{
  "status": "healthy"
}

```



### Chat

* **Endpoint:** `POST /chat`
* **Request:**
```json
{
  "message": "What is artificial intelligence?"
}

```


* **Response:**
```json
{
  "response": "Artificial intelligence is..."
}

```



### Testing the API

You can test the API directly using FastAPI's Swagger UI:
👉 Navigate to `http://127.0.0.1:8000/docs`, open the `POST /chat` endpoint, click **Try it out**, and provide a test message.

---

## Deployment

The application can be deployed with the frontend and backend hosted separately.

```text
Streamlit Community Cloud
        │
        │ HTTPS
        ▼
FastAPI Backend
        │
        ▼
LangChain
        │
        ▼
Groq LLM

```

* **Local Development:** The Streamlit frontend communicates with `http://127.0.0.1:8000/chat`.
* **Production:** The frontend should be configured to point to the publicly deployed FastAPI backend URL.

---

## Future Improvements

* [ ] Conversation memory
* [ ] Streaming responses
* [ ] Web search integration
* [ ] Agentic tool calling
* [ ] User authentication
* [ ] Persistent chat history
* [ ] Docker containerization
* [ ] Cloud deployment (Azure/AWS/GCP/Render)

---

## Author

**Mrityunjay Pathak**

```

```
