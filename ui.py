import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq LLM setup (LangChain wrapper)
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.5
)
# Trusted medical resources
resources = {
    "CDC": "https://www.cdc.gov",
    "WHO": "https://www.who.int",
    "Mayo Clinic": "https://www.mayoclinic.org"
}

# Streamlit UI
st.set_page_config(page_title="Healthcare Symptom Checker", page_icon="🩺")
st.title("🩺 Healthcare Symptom Checker Chatbot (Groq + LangChain)")
st.write("This chatbot provides **general information only**. It is not a medical diagnosis tool. Please consult a healthcare professional for medical advice.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
user_query = st.chat_input("Describe your symptoms...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Use Groq LLM to suggest possible conditions
    messages = [
        SystemMessage(content="You are a healthcare assistant. Provide general information only, not medical advice. Suggest possible conditions based on symptoms and point to trusted resources."),
        HumanMessage(content=user_query)
    ]
    response = llm(messages)
    answer = response.content

    # Append trusted resources
    answer += "\n\n🔗 Trusted resources:\n"
    for name, url in resources.items():
        answer += f"- [{name}]({url})\n"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").markdown(answer)
