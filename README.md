# 🏥 AI Voice Appointment Management System

An AI-powered Appointment Management System built using FastAPI, Streamlit, SQLAlchemy, Twilio, and Vapi.

The system allows users to:

- Schedule appointments
- Cancel appointments
- View appointments
- Interact through a web interface
- Book appointments through AI voice calls using Vapi and Twilio

---

# 🚀 Features

✅ Schedule Appointments

✅ Cancel Appointments

✅ List Appointments

✅ SQLite Database Integration

✅ FastAPI REST APIs

✅ Streamlit Frontend

✅ SQLAlchemy ORM

✅ Twilio Phone Number Integration

✅ Vapi AI Voice Assistant Integration

✅ Real-Time Appointment Booking Through Calls

---

# 🛠 Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

### Frontend
- Streamlit

### Voice AI
- Vapi
- Twilio

### Deployment Tools
- ngrok
- Uvicorn

---

# 📂 Project Structure

```bash
Voice_Agent/
│
├── backend.py
├── database.py
├── dummy_frontend.py
├── appointments.db
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Voice_Agent.git

cd Voice_Agent
```

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Backend

Start FastAPI server:

```bash
python backend.py
```

or

```bash
uvicorn backend:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# ▶️ Running Frontend

Start Streamlit app:

```bash
streamlit run dummy_frontend.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# 📌 API Endpoints

## Schedule Appointment

```http
POST /schedule_appointment/
```

Request:

```json
{
  "patient_name": "John",
  "reason": "General Checkup",
  "start_time": "2026-07-02T10:00:00"
}
```

---

## Cancel Appointment

```http
POST /cancel_appointment/
```

Request:

```json
{
  "patient_name": "John",
  "datetime": "2026-07-02T00:00:00"
}
```

---

## List Appointments

```http
POST /list_appointments/
```

Request:

```json
{
  "date": "2026-07-02"
}
```

---

# ☎️ AI Voice Integration

This project integrates:

### Twilio

Used for:

- Purchasing phone numbers
- Receiving incoming calls
- Connecting phone calls to AI

### Vapi

Used for:

- AI Voice Assistant
- Speech-to-Text
- Tool Calling
- Appointment Scheduling
- Appointment Cancellation
- Appointment Listing

---

# 🔄 Call Flow

```text
Customer Calls
        │
        ▼
Twilio Number
        │
        ▼
Vapi Assistant
        │
        ▼
FastAPI Tool Calls
        │
        ▼
SQLite Database
```

---

# 🧪 Example Conversation

```text
AI: Hello, how can I help you today?

User: I want to book an appointment.

AI: What is your name?

User: Pandu

AI: What is the reason for your appointment?

User: Fever

AI: What date and time would you like?

User: Tomorrow at 10 AM

AI: Your appointment has been successfully booked.
```

---

# 🔮 Future Enhancements

- Google Calendar Integration
- SMS Confirmation
- Email Notifications
- Multi-Doctor Support
- Appointment Rescheduling
- Authentication & Authorization
- Cloud Deployment



# 👨‍💻 Author
Pandu
GitHub:
https://github.com/pandu-21
