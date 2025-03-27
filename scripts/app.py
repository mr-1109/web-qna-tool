import streamlit as st
from bs4 import BeautifulSoup
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

# Config
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI API key not found. Please check your .env file.")
client = OpenAI(api_key=api_key)

# Session State to Save Q&A History
if 'qa_history' not in st.session_state:
    st.session_state.qa_history = []

# Function to shorten text preview
def text_preview(text, length=300):
    return text[:length] + ("..." if len(text) > length else "")

# Helper Functions
def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        page_soup = BeautifulSoup(response.content, 'html.parser')
        text_content = ' '.join(p.get_text(strip=True) for p in page_soup.find_all('p'))
        return text_content
    except Exception as e:
        return f"Error fetching {url}: {str(e)}"

def get_answer_from_context(context, question):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": (
                        "You are a helpful assistant. Answer the question below using ONLY the provided context.\n"
                        "If the answer is not available in the context, say 'The answer is not available in the provided context.'\n"
                        f"Context:\n{context}\n\nQuestion: {question}"
                    )
                }
            ]
        )
        return completion.choices[0].message.content#.strip()
    except Exception as e:
        return f"OpenAI API Error: {e}"

# Streamlit UI with Enhanced Styling
st.set_page_config(page_title="Web Q&A", layout="wide")

st.markdown("""
    <style>
        .main { background-color: #f4f6f9; padding: 2rem; border-radius: 10px; }
        .stTextInput > div > div > input {
            padding: 10px;
        }
        .stTextArea > div > textarea {
            padding: 10px;
        }
        .css-1d391kg, .css-1kyxreq, .stButton > button {
            font-size: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📘 Web Content Q&A Tool")

with st.container():
    st.markdown("### 🌐 Step 1: Enter URLs")
    urls_input = st.text_area("Enter one or more URLs (one per line):", height=100)

    st.markdown("### ❓ Step 2: Ask Your Question")
    question = st.text_input("Enter your question based on the website content:")

    if st.button("Get Answer"):
        with st.spinner("🔄 Fetching content and generating answer..."):
            urls = [url.strip() for url in urls_input.splitlines() if url.strip()]
            full_text = ""
            sources = []

            for url in urls:
                page_text = extract_text_from_url(url)
                if page_text:
                    full_text += f"\n\nFrom: {url}\n" + page_text
                    sources.append(f"\n🔗 **{url}**\n{text_preview(page_text)}")

            if not full_text.strip():
                st.error("❌ No content could be fetched from the provided URLs.")
            else:
                answer = get_answer_from_context(full_text, question)

                # Save to session history
                st.session_state.qa_history.append({
                    "question": question,
                    "answer": answer,
                    "sources": sources
                })

                st.success("✅ Answer Generated")
                st.markdown("### 💬 Answer:")
                st.markdown(f"<div style='padding:1rem; background-color:#fff; border-left:4px solid #4CAF50; border-radius:5px;'>{answer}</div>", unsafe_allow_html=True)

                with st.expander("📝 Context Used (from the webpages)"):
                    st.text_area("Context", value=full_text, height=300)

                if sources:
                    with st.expander("🔍 Sources Highlighted"):
                        for s in sources:
                            st.markdown(s, unsafe_allow_html=True)

# Display Q&A History
if st.session_state.qa_history:
    st.markdown("---")
    st.markdown("## 🧾 Q&A History")
    for idx, item in enumerate(reversed(st.session_state.qa_history), 1):
        st.markdown(f"**{idx}. Q:** {item['question']}")
        st.markdown(f"**A:** {item['answer']}")
        with st.expander("Show Sources"):
            for s in item['sources']:
                st.markdown(s, unsafe_allow_html=True)

st.markdown("""
---
📌 Answers rely **only** on the scraped content from the provided URLs
""")
