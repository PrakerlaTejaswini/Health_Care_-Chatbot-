# 🩺 Healthcare Symptom Checker Chatbot

An AI-powered Healthcare Symptom Checker built using **Streamlit**, **LangChain**, and **Groq Llama 3.3-70B**. The chatbot provides general health information based on user symptoms and recommends trusted medical resources such as **CDC**, **WHO**, and **Mayo Clinic**.

> **Disclaimer:** This application is for educational purposes only and does **not** provide medical diagnosis or treatment. Always consult a qualified healthcare professional for medical advice.

---

## 🚀 Features

- 💬 Interactive chatbot interface using Streamlit
- 🤖 Powered by **Groq Llama 3.3-70B Versatile**
- 🧠 Uses **LangChain** for LLM integration
- 🩺 Provides general information based on symptoms
- 🔗 Recommends trusted healthcare resources
- 💾 Maintains chat history during the session
- 🔐 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- Llama 3.3-70B Versatile
- python-dotenv

---

## 📂 Project Structure

```
Healthcare-Symptom-Checker/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Healthcare-Symptom-Checker.git

cd Healthcare-Symptom-Checker
```

---

### 2. Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Groq API

Create a `.env` file in the project directory.

```env
GROQ_API_KEY=your_groq_api_key_here
```

> **Important:** Never commit your `.env` file or API keys to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 💡 How It Works

### Step 1
Open the application.

### Step 2
Describe your symptoms in the chat box.

Example:

```
I have a fever, sore throat, and headache.
```

### Step 3

The chatbot:

- Understands the symptoms
- Suggests possible health conditions
- Explains the symptoms in simple language
- Provides links to trusted medical resources

### Step 4

Read the response and consult a healthcare professional if needed.

---

## 🧠 Application Workflow

```
                  User
                    │
                    ▼
          Enter Symptoms
                    │
                    ▼
            Streamlit Interface
                    │
                    ▼
               LangChain
                    │
                    ▼
       Groq Llama 3.3-70B Model
                    │
                    ▼
      General Health Information
                    │
                    ▼
   Trusted Medical Resource Links
                    │
                    ▼
            Response to User
```

---

## 📦 Requirements

```
streamlit
langchain
langchain-community
langchain-openai
python-dotenv
openai
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 📸 Application Preview

### Features

- 🩺 Symptom Checker
- 💬 Conversational Chat Interface
- 🤖 AI-powered Health Assistant
- 🔗 Trusted Medical Resources
- 📜 Chat History

---

## 🔒 Security

Store API keys securely using a `.env` file.

Example `.gitignore`

```
.env
__pycache__/
*.pyc
```

---

## ⚠️ Disclaimer

This chatbot is intended for informational and educational purposes only.

- It does **not** diagnose diseases.
- It does **not** replace a licensed medical professional.
- In case of emergency, contact your local emergency services or healthcare provider immediately.

---

## 🌍 Trusted Medical Resources

- **CDC** – https://www.cdc.gov
- **WHO** – https://www.who.int
- **Mayo Clinic** – https://www.mayoclinic.org

---

## 🚀 Future Enhancements

- Voice-based symptom input
- PDF medical report analysis
- Multi-language support
- Medical conversation memory
- Retrieval-Augmented Generation (RAG)
- Electronic Health Record (EHR) integration
- Doctor appointment recommendations
- Nearby hospital locator
- Medicine information lookup
- Downloadable chat history

---

## 👩‍💻 Author

**Tejaswini Prakerla**

- GitHub: https://github.com/PrakerlaTejaswini
- LinkedIn: https://www.linkedin.com/

---

## ⭐ If you found this project useful, please consider giving it a Star on GitHub!

---

## 📄 License

This project is licensed under the MIT License.
