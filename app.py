import os
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Connect to the database
db = SQLDatabase.from_uri("sqlite:///shop.db")

# Create the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create the SQL agent
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="openai-tools",
    verbose=True,
)


st.title("AI Chatbot for Database Analysis")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form for new question
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask about users, orders, products, or prices:", key="input")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    with st.spinner("Thinking..."):
        try:
            # Call your agent_executor with the user's input
            response = agent_executor.invoke({"input": user_input})
            # Adjust this line if your agent_executor returns a different structure
            answer = response.get("output", "Sorry, I didn't get a response.")
        except Exception as e:
            answer = f"Error: {e}"

        # Append to chat history
        st.session_state.chat_history.append({"user": user_input, "bot": answer})
# Now display the full chat history (including the latest exchange)
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
