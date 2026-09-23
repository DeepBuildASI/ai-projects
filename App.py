import streamlit as st
import json
from pathlib import Path
from datetime import datetime
from groq import Groq

# ---- Config ----
GROQ_API_KEY = "GROQ_API_KEY"
MODEL = "openai/gpt-oss-20b"

client = Groq(api_key=GROQ_API_KEY)

# ---- Page setup ----
st.set_page_config(
    page_title="ReviewReply",
    page_icon="💬",
    layout="centered"
)

# ---- Styling ----
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(180deg, #f6f8fc 0%, #eef1f8 100%);
    }

    /* Hide Streamlit branding */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* Main container */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 780px;
    }

    /* Title */
    .title {
        font-size: 2.4rem;
        font-weight: 700;
        letter-spacing: -1px;
        color: #0f172a;
        margin-bottom: 0.3rem;
    }
    .title span {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        color: #64748b;
        font-size: 1.05rem;
        margin-bottom: 2.5rem;
        font-weight: 400;
    }

    /* Labels */
    .label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #6366f1;
        font-weight: 700;
        margin-bottom: 0.5rem;
        margin-top: 1rem;
    }

    /* Text area */
    .stTextArea textarea {
        border-radius: 12px;
        border: 1.5px solid #e2e8f0;
        font-size: 15px;
        padding: 1rem;
        background: #ffffff;
        transition: all 0.2s ease;
        color: #0f172a;
    }
    .stTextArea textarea:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
    }

    /* Selectbox */
    .stSelectbox div[data-baseweb="select"] > div {
        border-radius: 12px;
        border: 1.5px solid #e2e8f0;
        background: #ffffff;
    }

    /* Button */
    .stButton button {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        color: white;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 15px;
        border: none;
        width: 100%;
        transition: all 0.25s ease;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35);
        letter-spacing: 0.3px;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5);
        color: white;
    }

    /* Reply card */
    .reply-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #6366f1;
        border-radius: 14px;
        padding: 1.5rem 1.7rem;
        margin-top: 0.8rem;
        font-size: 15.5px;
        line-height: 1.7;
        color: #1e293b;
        box-shadow: 0 2px 12px rgba(15, 23, 42, 0.05);
    }

    /* Saved badge */
    .saved-badge {
        display: inline-block;
        background: #ecfdf5;
        color: #059669;
        font-size: 0.78rem;
        font-weight: 600;
        padding: 0.3rem 0.75rem;
        border-radius: 20px;
        margin-top: 0.8rem;
        border: 1px solid #a7f3d0;
    }

    /* Divider */
    hr {
        border: none;
        border-top: 1px solid #e2e8f0;
        margin: 2.5rem 0;
    }

    /* History cards */
    .history-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.1rem 1.3rem;
        margin-bottom: 0.9rem;
    }
    .history-time {
        font-size: 0.75rem;
        color: #94a3b8;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    .history-review {
        font-size: 0.92rem;
        color: #475569;
        font-style: italic;
        margin-bottom: 0.6rem;
        padding-left: 0.8rem;
        border-left: 2px solid #e2e8f0;
    }
    .history-reply {
        font-size: 0.95rem;
        color: #0f172a;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown('<div class="title">Review<span>Reply</span></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Turn customer reviews into professional replies in seconds.</div>', unsafe_allow_html=True)

# ---- Input ----
st.markdown('<div class="label">Customer review</div>', unsafe_allow_html=True)
review = st.text_area(
    "review_input",
    label_visibility="collapsed",
    height=160,
    placeholder="Paste the customer review here..."
)

business_type = st.selectbox(
    "Business type",
    ["Dental clinic", "Restaurant", "Salon", "Real estate agency", "Gym", "Other"]
)

generate = st.button("✨ Generate reply")

# ---- Output ----
if generate and review.strip():
    prompt = f"""You are the owner of a {business_type.lower()}.
Write a short, professional, human reply to this customer review.
Match the tone: if the review is angry, be apologetic. If happy, be grateful.
Keep it under 4 sentences. Do not use corporate jargon.
Do not mention that you are an AI.

Review: {review}
"""
    with st.spinner("Writing reply..."):
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content

    # Save
    history_file = Path("replies.json")
    history = json.loads(history_file.read_text()) if history_file.exists() else []
    history.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "business_type": business_type,
        "review": review,
        "reply": reply
    })
    history_file.write_text(json.dumps(history, indent=2))

    st.markdown('<div class="label">Reply</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="reply-card">{reply}</div>', unsafe_allow_html=True)
    st.markdown('<div class="saved-badge">✓ Saved to history</div>', unsafe_allow_html=True)

elif generate:
    st.warning("Please paste a review first.")

# ---- History ----
history_file = Path("replies.json")
if history_file.exists():
    history = json.loads(history_file.read_text())
    if history:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="label">Recent replies</div>', unsafe_allow_html=True)
        for item in reversed(history[-5:]):
            st.markdown(f"""
                <div class="history-card">
                    <div class="history-time">{item['time']} · {item['business_type']}</div>
                    <div class="history-review">"{item['review'][:120]}{'...' if len(item['review']) > 120 else ''}"</div>
                    <div class="history-reply">{item['reply']}</div>
                </div>
            """, unsafe_allow_html=True)