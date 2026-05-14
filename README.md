# Customer Support AI Agent with FastAPI + LangChain + ChromaDB

Production-style minimal AI customer support backend.

---

## Tech Stack

- FastAPI
- LangChain
- OpenAI
- ChromaDB
- RAG (Retrieval-Augmented Generation)

---

## Features

✅ FastAPI Backend  
✅ REST API  
✅ ChromaDB Vector Database  
✅ LangChain RAG Pipeline  
✅ Escalation Logic  
✅ Frontend Ready  
✅ Minimal & Clean Architecture  

---

## Project Structure

```
customer_support_ai_agent_v2/
│
├── data/
│   └── faqs.txt
│
├── chroma_db/
├── knowledge_base.py
├── agent.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Add API Key

Create `.env` file:

```env
OPENAI_API_KEY=your_openai_key
```

---

## Build ChromaDB

```bash
python knowledge_base.py
```

---

## Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

## API Endpoints

### Health Check

```
GET /
```

---

### Chat Endpoint

```
POST /chat
```

Request:
```json
{
  "message": "How can I reset my password?"
}
```

Response:
```json
{
  "success": true,
  "escalated": false,
  "answer": "Click Forgot Password on the login page."
}
```

---

## Test API

Open:

```
http://127.0.0.1:8000/docs
```

FastAPI Swagger UI will open automatically.

---

## Frontend Integration

You can connect this backend with:
- React
- Next.js
- Vue
- Angular
- Flutter
- React Native

Example frontend request:

```javascript
const response = await fetch("http://127.0.0.1:8000/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    message: "What is your refund policy?"
  })
});

const data = await response.json();

console.log(data);
```

---

## Flow

Load knowledge base (faqs.txt)
Split into chunks
Convert chunks → vector embeddings
Store embeddings in ChromaDB
User asks question
Convert question → embedding
Retrieve most relevant chunks from Chroma
Pass:
user question
retrieved context
to OpenAI LLM
LLM generates grounded answer