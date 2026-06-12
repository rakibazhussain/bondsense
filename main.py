from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    chat: str


@app.get("/")
def home():
    return {"message": "Love Analysis API Running"}


@app.post("/analyze")
def analyze(data: ChatRequest):

    chat = data.chat.lower()

    love_score = 30
    flirting_score = 20

    romantic_words = [
        "love",
        "miss you",
        "baby",
        "babe",
        "darling",
        "cute",
        "beautiful",
        "sweetheart",
        "❤️",
        "😍",
        "😘"
    ]

    friendzone_words = [
        "bro",
        "buddy",
        "friend",
        "bestie",
        "dude"
    ]

    red_flag_words = [
        "hate",
        "leave me alone",
        "stop texting",
        "annoying",
        "go away"
    ]

    for word in romantic_words:
        if word in chat:
            love_score += 10
            flirting_score += 10

    love_score = min(love_score, 100)
    flirting_score = min(flirting_score, 100)

    friendzone_probability = 20

    for word in friendzone_words:
        if word in chat:
            friendzone_probability += 20

    friendzone_probability = min(friendzone_probability, 100)

    red_flag_score = 5

    for word in red_flag_words:
        if word in chat:
            red_flag_score += 25

    red_flag_score = min(red_flag_score, 100)

    # Conversation Balance

    a_count = 0
    b_count = 0

    lines = data.chat.split("\n")

    for line in lines:
        line = line.strip()

        if line.lower().startswith("a:"):
            a_count += 1

        elif line.lower().startswith("b:"):
            b_count += 1

    total = a_count + b_count

    if total == 0:
        conversation_balance = 50
    else:
        difference = abs(a_count - b_count)
        conversation_balance = max(
            0,
            int(100 - ((difference / total) * 100))
        )

    if love_score > 70:
        summary = "Strong romantic interest detected ❤️"

    elif friendzone_probability > 70:
        summary = "Looks more like friendship than romance 😊"

    elif red_flag_score > 50:
        summary = "Potential communication red flags detected 🚩"

    else:
        summary = "Mixed signals detected. More conversation needed."

    return {
        "love_score": love_score,
        "one_sided_score": 100 - love_score,
        "flirting_score": flirting_score,
        "friendzone_probability": friendzone_probability,
        "red_flag_score": red_flag_score,
        "conversation_balance": conversation_balance,
        "messages_from_a": a_count,
        "messages_from_b": b_count,
        "summary": summary
    }