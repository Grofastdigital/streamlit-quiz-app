import streamlit as st
import pandas as pd
from datetime import datetime

# ---------- CONFIG ----------
st.set_page_config(page_title="📝 Advanced Quiz App", page_icon="📝", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #8EC5FC, #E0C3FC);
        padding: 20px;
        border-radius: 15px;
        color: #333;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("📝 Advanced Quiz App with Leaderboard")

# ---------- QUESTIONS ----------
questions = [
    {
        "question": "Which programming language is used in Streamlit?",
        "options": ["Java", "Python", "C++", "Go"],
        "answer": "Python"
    },
    {
        "question": "Which library is commonly used for data analysis in Python?",
        "options": ["Pandas", "Numpy", "Matplotlib", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Who developed the Python language?",
        "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "Sundar Pichai"],
        "answer": "Guido van Rossum"
    }
]

# ---------- USER INFO ----------
name = st.text_input("Enter your name to start the quiz:")

if name:
    score = 0
    answers = []

    for idx, q in enumerate(questions):
        st.subheader(f"Q{idx + 1}: {q['question']}")
        user_answer = st.radio("Select your answer:", q["options"], key=idx)
        answers.append(user_answer)

    if st.button("Submit Quiz 🚀"):
        for idx, q in enumerate(questions):
            if answers[idx] == q["answer"]:
                score += 1

        st.success(f"🎉 {name}, you scored {score} out of {len(questions)}")
        st.balloons()

        # ---------- SAVE TO LEADERBOARD ----------
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_entry = pd.DataFrame([[name, score, timestamp]], columns=["Name", "Score", "Timestamp"])
        try:
            leaderboard = pd.read_csv("leaderboard.csv")
            leaderboard = pd.concat([leaderboard, new_entry], ignore_index=True)
        except FileNotFoundError:
            leaderboard = new_entry

        leaderboard.to_csv("leaderboard.csv", index=False)

        st.subheader("🏆 Leaderboard")
        st.dataframe(leaderboard.sort_values(by="Score", ascending=False).reset_index(drop=True))

st.markdown("</div>", unsafe_allow_html=True)
