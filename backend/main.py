import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import asyncio

# --------------------
# Initialize Sentry
# --------------------
sentry_sdk.init(
    dsn="https://d328c16a92ae6661b8435920c825a9fe@o4510098511626240.ingest.us.sentry.io/4510103469359104",  # Replace with your Sentry DSN
    traces_sample_rate=1.0
)

# --------------------
# FastAPI app
# --------------------
app = FastAPI(title="React + FastAPI Demo with Sentry")

# Wrap with Sentry ASGI middleware
app.add_middleware(SentryAsgiMiddleware)

# --------------------
# Enable CORS for React dev server
# --------------------
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

# --------------------
# Routes
# --------------------
@app.get("/")
def root():
    return {"message": "FastAPI backend is running"}

@app.get("/error1")
def error1():
    raise HTTPException(status_code=500, detail="Deliberate server error 1")

@app.get("/error2")
def error2():
    raise Exception("Deliberate unhandled exception 2")

@app.get("/slow")
async def slow():
    await asyncio.sleep(6)
    return {"message": "This endpoint intentionally slept for 6 seconds"}
