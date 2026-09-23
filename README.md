# ReviewReply

> Turn customer reviews into professional replies in seconds.

ReviewReply is a lightweight web app that generates polished, human-sounding responses to customer reviews. Built for small businesses — clinics, restaurants, salons, gyms — that need to respond to reviews fast without sounding robotic or corporate.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.64-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## What it does

- Paste any customer review
- Select your business type
- Click **Generate reply**
- Get a short, professional, tone-matched response in under 3 seconds
- Every reply is saved to a local history you can browse

The model reads the review and decides tone automatically — angry reviews get an apologetic reply, happy reviews get a grateful one. No templates. No hardcoded strings.

---

## Why it exists

Small businesses lose customers over bad review replies. Hiring someone to manage this costs money. Using generic AI tools makes replies sound fake.

ReviewReply is:
- **Fast** — one click, one reply
- **Natural** — written like a real business owner, not a bot
- **Private** — runs locally, no third-party dashboards
- **Simple** — no account, no signup, no clutter

---

## Tech stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| LLM | Groq (`openai/gpt-oss-20b`) |
| Config | python-dotenv |
| Storage | JSON (local) |
| Language | Python 3.13 |

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/DeepBuildASI/review-reply-agent.git
cd review-reply-agent
```

### 2. Create a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Add your Groq API key

Get a free key at [console.groq.com/keys](https://console.groq.com/keys).

Create a file named `.env` in the project root:

```
GROQ_API_KEY=gsk_your_key_here
```

### 5. Run

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`.

---

## Project structure

```
review-reply-agent/
├── app.py               # Streamlit UI + logic
├── requirements.txt     # Dependencies
├── .env                 # API key (not committed)
├── .gitignore
└── replies.json         # Auto-generated history
```

---

## How it works

1. User pastes a review and picks a business type
2. A dynamic prompt is built and sent to Groq's LLM
3. The model reads the review, detects tone, and writes a reply
4. The reply is displayed and appended to `replies.json`
5. The last 5 replies are shown in a clean history section

No hardcoded replies. No templates. The model does the writing.

---

## Roadmap

- [ ] Connect to live Google Reviews via Places API
- [ ] WhatsApp and email integration
- [ ] Multi-user accounts with Stripe billing
- [ ] Custom brand voice per business
- [ ] Export replies as CSV

---

## License

MIT — free to use, modify, and ship.

---

## Author

**Asma Rizwan Rao** ([@DeepBuildASI](https://github.com/DeepBuildASI))
Built as a real product, not a tutorial project.