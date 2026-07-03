import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in .env")
    st.stop()

# ----------------------------
# LLM
# ----------------------------
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3,
)

# ----------------------------
# Trusted Resources
# ----------------------------
resources = {
    "CDC": "https://www.cdc.gov",
    "WHO": "https://www.who.int",
    "Mayo Clinic": "https://www.mayoclinic.org",
}

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Healthcare AI Assistant",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 AI Healthcare Symptom Checker")

st.info(
    "⚠ This chatbot provides educational information only. "
    "It is NOT a medical diagnosis."
)

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.header("Common Symptoms")

selected = st.sidebar.multiselect(
    "Select Symptoms",
    [
        "Fever",
        "Cough",
        "Headache",
        "Sore Throat",
        "Body Pain",
        "Vomiting",
        "Diarrhea",
        "Fatigue",
        "Chest Pain",
        "Shortness of Breath",
        "Dizziness",
        "Cold",
        "Runny Nose",
    ]
)

st.sidebar.markdown("---")

st.sidebar.subheader("Trusted Websites")

for name, url in resources.items():
    st.sidebar.markdown(f"- [{name}]({url})")

# ----------------------------
# Chat Memory
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# ----------------------------
# User Input
# ----------------------------

user_query = st.chat_input("Describe your symptoms...")

if user_query:

    if selected:
        symptoms = ", ".join(selected)
        user_query = f"My symptoms are: {symptoms}. {user_query}"

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )

    st.chat_message("user").markdown(user_query)

    prompt = """
You are an AI Healthcare Symptom Checker.

Never diagnose diseases.

Always answer using the following format.

# 🩺 Possible Conditions

List 3-5 possible conditions.

# 📖 Explanation

Explain each condition briefly.

# ⚠ Severity Level

Mention whether symptoms appear

• Low

• Medium

• High

# 💊 Self-Care

Provide safe home-care advice.

# 🚨 Emergency Warning

Mention when immediate medical attention is required.

# 👨‍⚕ Recommendation

Recommend consulting a doctor.

# ⚠ Disclaimer

This is educational information only and not a medical diagnosis.
"""

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=user_query)
    ]

    try:

        with st.spinner("Analyzing symptoms..."):

            response = llm.invoke(messages)

            answer = response.content

            answer += "\n\n---\n"

            answer += "### 🔗 Trusted Medical Resources\n"

            for name, url in resources.items():
                answer += f"- [{name}]({url})\n"

    except Exception as e:

        answer = f"❌ Error:\n\n{e}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.chat_message("assistant").markdown(answer)
