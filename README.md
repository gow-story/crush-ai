
---

```markdown
# 💬 Crush AI

> Analyze dating conversations using AI to uncover intent, effort, and emotional tone — with a twist of personality.

## What It Does

Crush AI is a FastAPI-powered backend that takes a dating conversation transcript and analyzes it through one of four distinct "modes" — each giving you a different perspective on what's really going on.

Paste in a conversation, pick your mode, and get back a structured breakdown of:

- **Interest Level** — How interested does the other person seem?
- **Effort Balance** — Who's putting in more work?
- **Tone** — What's the emotional vibe of the conversation?
- **Reality Check** — An honest assessment of the situation
- **Advice** — What you should do next

## Analysis Modes

| Mode | Personality |
|------|-------------|
| `mom` | Caring, protective, warm — slightly worried about you |
| `friend` | Honest, supportive, direct — tells it like it is |
| `brutal` | Blunt and slightly savage — but not cruel |
| `analyst` | Structured, logical, data-driven — no fluff |

## Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — REST API framework
- **[OpenAI GPT-4.1 Mini](https://openai.com/api/)** — Powers the conversation analysis
- **[Uvicorn](https://www.uvicorn.org/)** — ASGI server
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — Environment variable management

## Getting Started

### Prerequisites

- Python 3.8+
- An OpenAI API key

### Installation

```bash
# Clone the repo
git clone https://github.com/gow-story/crush-ai.git
cd crush-ai

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your OpenAI API key to .env:
# OPENAI_API_KEY=your_key_here
```

### Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Reference

### `GET /`
Health check — confirms the server is running.

**Response:**
```json
{ "message": "Crush AI is running" }
```

---

### `POST /analyze-texts`
Analyzes a conversation transcript in the selected mode.

**Request Body:**
```json
{
  "transcript": "Hey! Are you free Saturday?\nYeah maybe, what did you have in mind?\nI was thinking dinner?\nSure sounds good.",
  "mode": "friend"
}
```

**Response:**
```json
{
  "interest_level": "Moderate — they're open but not enthusiastic",
  "effort_balance": "You're initiating more; they're responding but not driving",
  "tone": "Casual and noncommittal",
  "reality_check": "They said yes, but the energy is lukewarm. Don't over-invest yet.",
  "advice": "Go to dinner, keep it light, and see if they show up differently in person."
}
```

**Available modes:** `mom`, `friend`, `brutal`, `analyst`

## Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Project Structure

```
crush-ai/
├── main.py           # FastAPI app, routes, and OpenAI integration
├── requirements.txt  # Python dependencies
└── .env              # Your API keys (not committed)
```

## Future Ideas

- Frontend UI for pasting conversations
- Support for more analysis modes
- Conversation history tracking
- Integration with messaging platforms
```

---

Want me to also push this directly to the repo, replacing the empty README? Just say the word!
