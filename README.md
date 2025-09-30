---

# React + FastAPI Error Monitoring Demo with Sentry, Vertex AI, and Slack Integration

This repository demonstrates a simple **React + FastAPI** application integrated with **Sentry** for error monitoring and performance tracking, a **FastAPI webhook** that uses **Vertex AI** for automated error summarization, and posting results to **Slack/Teams**. It also includes a mini **RAG system** using FAISS for referencing troubleshooting notes.

---

## Features

* **React Frontend**

  * Basic UI to trigger FastAPI endpoints
  * Button to deliberately trigger errors and slow endpoints

* **FastAPI Backend**

  * Serves API endpoints with Sentry integration
  * Two deliberate error endpoints
  * One slow endpoint for performance testing
  * Webhook endpoint calling Vertex AI for automated error summarization

* **Sentry Integration**

  * Captures exceptions and performance metrics
  * Demonstrates error grouping and duplicate error handling

* **Vertex AI + RAG Mini System**

  * Summarizes errors in ≤120 words
  * Lists 3 recommended next steps
  * Uses FAISS to retrieve troubleshooting notes (5–10 stored entries)

* **Slack/Teams Integration**

  * Sends error summaries and suggested actions to a configured webhook

---

## Prerequisites

* Python 3.10+
* Node.js 18+ / npm
* Google Cloud account with Vertex AI access
* Slack or Teams workspace with an incoming webhook URL

---

## Setup

### Backend (FastAPI)

1. Navigate to the backend folder:

```bash
cd backend
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set environment variables:

```bash
export SENTRY_DSN=<your_sentry_dsn>
export SLACK_WEBHOOK=<your_slack_webhook_url>
export GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_json>
export VERTEX_AI_ENDPOINT=<your_vertex_ai_endpoint_id>
```

5. Run the FastAPI server:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Frontend (React)

1. Navigate to the frontend folder:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Run the React app:

```bash
npm start
```

---

## Usage

1. Open the frontend at [http://localhost:3000](http://localhost:3000)
2. Click buttons to:

   * Trigger deliberate errors
   * Trigger a slow endpoint
3. Observe errors captured in Sentry
4. Check Slack/Teams for automated error summaries

---

## Screenshots

![Slack Message Screenshot](./screenshots/slack_message.png)

---

## Notes on PII Scrubbing

* All sensitive information such as user identifiers, emails, and passwords are **redacted** before sending data to Sentry, Vertex AI, or Slack.
* PII is replaced with placeholders or hashed values.
* Error grouping uses **error type + stack trace similarity**, ignoring dynamic PII elements to consolidate duplicates.

---

## Repository Structure

```
.
├── backend/          # FastAPI backend
│   ├── main.py
│   ├── requirements.txt
│   └── ...
├── frontend/         # React frontend
│   ├── src/
│   ├── package.json
│   └── ...
├── screenshots/      # Slack/Teams message screenshots
└── README.md
```





### 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/timeguard-validator.git
cd timeguard-validator
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

> Access the API at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 5. Run Frontend (Streamlit)

```bash
streamlit run frontend/app.py
```

> Access the Dashboard at: [http://localhost:8501](http://localhost:8501)

---

## 📤 API Endpoints

### ✅ Upload Timesheet

**POST** `/timesheets`
**Payload**: CSV file with the following columns:

* `date` (YYYY-MM-DD)
* `start` (HH\:MM)
* `end` (HH\:MM)
* `project` (string)

---

### 📅 Get Calendar Events

**GET** `/calendar/events?date=YYYY-MM-DD`
**Returns**:

```json
[
  {
    "id": "uuid",
    "title": "Project Work",
    "start": "2025-08-01T09:00:00",
    "end": "2025-08-01T10:00:00"
  },
  ...
]
```

---

### 📊 Get Validation Report

**GET** `/reports/{id}`
**Returns**:

```json
{
  "missingEntries": [...],
  "extraEntries": [...]
}
```

---

## 🧪 Testing

To run all tests:

```bash
pytest tests/
```

**Test coverage includes:**

* Timesheet parser
* Calendar event generator
* Validation logic

---

## 📸 UI Features

* 📁 Upload CSV file
* 📅 Generate mock calendar
* ✅ Highlights matched entries
* 🚨 Flags missing or extra time blocks
* 📊 View structured report with color-coded tables

---

## 🧠 Mock Calendar Data

If real calendar integration (e.g., Google Calendar API) isn't used, the system will:

* Generate 1–2 random project blocks per day
* Between 9AM and 5PM
* With 1-hour event durations

You can customize this logic inside the `generate_mock_calendar()` function in `app.py`.

---

## 📚 Future Enhancements

* 🔐 User authentication
* 📆 Real calendar integration (Google, Outlook)
* 📤 Export validation reports to Excel/PDF
* 📊 Analytics dashboard for HR/Managers

---

## 🤖 prompt\_log.md

If any AI/LLM-generated logic or text is used (e.g., prompt engineering, autogenerated tests or descriptions), please log the prompt and source in the file `prompt_log.md`.

---

## 🧑‍💻 Contributors

* [Harikrishna Panneerselvam – LinkedIn](https://www.linkedin.com/in/harikrishna-panneerselvam-09056b1b3/)

Feel free to open issues or contribute via pull requests!

