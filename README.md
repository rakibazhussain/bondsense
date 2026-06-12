# 💙 BondSense

> Understand the emotions behind your conversations using AI-powered relationship intelligence.


## ✨ What is BondSense?

BondSense is an AI-powered conversation intelligence platform that analyzes chat messages between two people and generates emotional insights such as love intensity, flirting level, friendzone probability, red flags, and conversation balance.

It transforms raw conversations into structured emotional signals using a rule-based NLP engine and presents results in a clean, interactive dashboard.

---

## 🚀 Key Features

### ❤️ Emotional Intelligence
- Love Score Detection (0–100)
- Flirting Intensity Analysis
- One-Sided Relationship Detection

### 👥 Relationship Insights
- Friendzone Probability Estimation
- Red Flag Detection in conversations
- AI-generated conversation summary

### ⚖️ Communication Analytics
- Message balance between Person A & B
- Engagement comparison scoring

### 📊 Interactive Dashboard
- Real-time results rendering
- Progress-bar based visual analytics
- Pre-built sample conversations for instant testing

---

## 🧠 How It Works

1. User inputs a conversation  
2. React frontend sends data to FastAPI backend  
3. Backend processes text using keyword-based NLP rules  
4. System calculates emotional and relational scores  
5. JSON response is sent back to frontend  
6. Dashboard visualizes the insights instantly  

---

## 🛠️ Tech Stack

### Frontend
- React (Vite)
- Axios
- CSS

### Backend
- FastAPI
- Python
- Pydantic
- CORS Middleware

### Intelligence Layer
- Rule-based NLP (keyword sentiment detection)
- Conversation structure analysis

---

## 📡 API Reference

### GET /
Health check endpoint

Response:
```json
{
  "message": "Love Analysis API Running"
}


BondSense is an early-stage AI product exploring emotional intelligence in digital conversations.
