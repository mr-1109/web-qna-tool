# 📘 Web Content Q&A Tool

This is a Streamlit web app that lets you ask questions based solely on the content from any URL(s) you provide. It fetches and processes webpage content, sends it to OpenAI's GPT-4 model, and returns concise answers — with no external assumptions.

---

## 🚀 Features

- 🔗 Input one or more URLs
- 🤖 Ask questions and get answers using **GPT-4o**
- 💾 Q&A history stored during the session
- 📝 Source text previews highlighted for transparency
- 🌙 Sleek and minimal UI

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/mr-1109/web-qna-tool.git
cd web-qna-tool
```

### 2. Create & activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the project root

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**❗Do NOT commit this file to GitHub. It contains sensitive data.**

---

## ▶️ Run the App Locally

```bash
streamlit run app.py
```

---

## 🌐 Deploy to Streamlit Cloud

1. Push your code to GitHub (excluding `.env`)
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo and set your `OPENAI_API_KEY` as a **secret**
4. Deploy!

---

## 📌 Notes

- Answers are generated *only* from the content of the webpages provided.
- Your API key will never be exposed if handled securely using `.env` or Streamlit secrets.

---

## 🛡️ .gitignore Sample

```gitignore
__pycache__/
*.pyc
.env
.env.*
```

---

## ✨ Future Improvements

- [ ] Highlight answer text with source reference
- [ ] Export chat history as PDF or CSV
- [ ] Multi-language support

---

## 👨‍💻 Author

**Rohit Patel**  
[GitHub](https://github.com/mr-1109) | [LinkedIn]([https://linkedin.com/in/rahul-patel](https://www.linkedin.com/in/rohit-kumar-patel-350a0383/))

---

## 🪪 License

This project is open source under the [MIT License](LICENSE).
