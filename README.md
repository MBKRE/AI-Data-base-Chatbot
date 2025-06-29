# AI-Data-base-Chatbot
A lightweight AI-powered chatbot built to handle natural language conversations. Supports context-aware responses, customizable prompts, and easy API integration. Ideal for customer support, virtual assistants, or internal tools.

A Streamlit-based chatbot interface that uses **LangChain**, **OpenAI GPT-3.5**, and a **SQLite database** to allow users to ask natural language questions about their data — and get accurate answers via automatically generated SQL queries.

---

## Features

- Ask natural language questions (e.g., *"What’s the average product price?"*)
- Backed by OpenAI's GPT-3.5 for powerful natural language understanding
- Connects directly to a SQLite database (`shop.db`)
- Automatically converts questions to SQL using LangChain’s SQL Agent
- Clean web UI powered by Streamlit
- Chat history preserved during session

---

## Tech Stack

- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-3.5](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)
- [SQLite](https://www.sqlite.org/index.html)
- [Python](https://www.python.org/)
- `.env` for environment variable management

---

## 📂 Project Structure


├── app.py # Main app script
├── sqlitedb.py # SQLite database file
├── .env # Contains your OpenAI API key
├── requirements.txt # Python dependencies
└── README.md # You're here!



---

## 📦 Installation

### 1. Clone the repo

bash
git clone https://github.com/MBKRE/ai-database-chatbot.git
cd ai-database-chatbot

2. Install dependencies 
pip install -r requirements.txt

3. Add your OpenAI API key
Create a .env file in the root directory:

4.Add your OpenAI API key
Create a .env file in the root directory:

5.Add your OpenAI API key
Create a .env file in the root directory:

6.Create a .env file in the root directory:
OPENAI_API_KEY= xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

7.Run the app
streamlit run main.py
