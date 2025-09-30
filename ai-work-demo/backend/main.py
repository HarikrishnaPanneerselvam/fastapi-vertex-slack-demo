# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI(title="Demo errors")

# allow React dev server
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/error1")
def error1():
    # a handled server error (returns JSON with detail)
    raise HTTPException(status_code=500, detail="Deliberate server error 1")


@app.get("/error2")
def error2():
    # an unhandled exception (will produce a 500 and stacktrace in the server logs)
    raise Exception("Deliberate unhandled exception 2")


@app.get("/slow")
async def slow():
    # intentionally slow: sleeps for 6 seconds
    await asyncio.sleep(6)
    return {"message": "This endpoint intentionally slept for 6 seconds"}


# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from google.auth.transport.requests import Request
from google.oauth2 import service_account

app = FastAPI()

# Load your mini-RAG (FAISS) here if needed
# from rag_store import load_rag_store
# rag_db = load_rag_store()

PROJECT_ID = "inspiring-team-472217-n0"
LOCATION = "us-central1"
SERVICE_ACCOUNT_FILE = "E:\Irmai-Documents\Irmai\AI-Work-Experience\vertex_service_account.json"

class ErrorPayload(BaseModel):
    error_message: str

def call_vertex_ai(prompt_text):
    # Authenticate using service account
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    token = credentials.token

    url = f"https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/gemini-1.5-flash:predict"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {"instances": [{"content": prompt_text}]}

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    return resp.json()

@app.post("/webhook")
async def handle_error(payload: ErrorPayload):
    # Example: add RAG context if needed
    # docs = rag_db.similarity_search(payload.error_message, k=3)
    # rag_context = "\n".join([f"- {d.page_content} (Ref: {d.metadata['url']})" for d in docs])
    # prompt = f"Error: {payload.error_message}\nContext:\n{rag_context}\nSummarize in ≤120 words, list 3 next steps, include citations."

    # Simple prompt without RAG for testing
    prompt = f"Error: {payload.error_message}\nSummarize in ≤120 words, list 3 next steps."

    response = call_vertex_ai(prompt)
    return {"vertex_ai_response": response}
