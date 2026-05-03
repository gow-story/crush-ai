from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later replace with your WordPress domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AnalyzeRequest(BaseModel):
    transcript: str
    mode: str

MODES = {
    "mom": "Respond like a caring, protective mom. Warm, emotional, slightly worried.",
    "friend": "Respond like a close friend. Honest, supportive, direct.",
    "brutal": "Respond bluntly, slightly savage, but not cruel.",
    "analyst": "Respond like a data analyst. Structured, logical, concise."
}

@app.get("/")
def home():
    return {"message": "Crush AI is running"}

@app.post("/analyze-texts")
def analyze_texts(request: AnalyzeRequest):
    transcript = request.transcript
    mode = request.mode

    tone = MODES.get(mode, "Respond clearly and concisely.")

    prompt = f"""
You are analyzing a dating conversation.

Mode:
{tone}

Return ONLY valid JSON. No explanation.

Format:
{{
  "interest_level": "...",
  "effort_balance": "...",
  "tone": "...",
  "reality_check": "...",
  "advice": "..."
}}

Be concise. Honest.

Conversation:
{transcript}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Return only valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    raw_output = response.choices[0].message.content

    try:
        parsed_output = json.loads(raw_output)
    except:
        return {"error": "Failed to parse response", "raw": raw_output}

    return parsed_output