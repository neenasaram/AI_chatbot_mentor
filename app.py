import streamlit as st
from datetime import datetime
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# ---------------------------------
# Load environment variables (.env)
# ---------------------------------
load_dotenv()

# ---------------------------------
# Streamlit Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="AI Chatbot Mentor",
    page_icon="🤖",
    layout="centered"
)

# ---------------------------------
# Module Definitions
# ---------------------------------
MODULES = {
    "Python": "Python programming, syntax, data types, control flow, functions, OOP, file handling, libraries.",
    "SQL": "SQL queries, joins, subqueries, constraints, indexing, normalization, databases.",
    "Power BI": "Power BI dashboards, DAX, Power Query, data modeling, reports, visualizations.",
    "Exploratory Data Analysis (EDA)": "Data cleaning, statistics, pandas, numpy, matplotlib, seaborn.",
    "Machine Learning (ML)": "Supervised, unsupervised learning, feature engineering, evaluation, models.",
    "Deep Learning (DL)": "Neural networks, CNN, RNN, backpropagation, TensorFlow, PyTorch.",
    "Generative AI (Gen AI)": "LLMs, transformers, prompt engineering, fine-tuning, RAG.",
    "Agentic AI": "LLM agents, tools, planning, reasoning, autonomous workflows."
}

# ---------------------------------
# Session State Initialization
# ---------------------------------
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="history",
        return_messages=True
    )

# ---------------------------------
# Welcome Screen
# ---------------------------------
if st.session_state.selected_module is None:
    st.title("👋 Welcome to AI Chatbot Mentor")
    st.subheader("Your personalized AI learning assistant")
    st.markdown("Please select a learning module to begin your mentoring session.")

    selected = st.selectbox("📌 Available Modules", list(MODULES.keys()))

    if st.button("Start Mentoring"):
        st.session_state.selected_module = selected
        st.rerun()

# ---------------------------------
# Module Mentor Interface
# ---------------------------------
else:
    module = st.session_state.selected_module
    domain = MODULES[module]

    st.title(f"🎯 Welcome to {module} AI Mentor")
    st.markdown(f"I am your **dedicated mentor** for **{module}**.")
    st.markdown("Ask your questions below 👇")

    # ---------------------------------
    # Prompt Template (STRICT CONTROL)
    # ---------------------------------
    prompt = PromptTemplate(
        input_variables=["history", "question"],
        template=f"""
You are an AI mentor strictly limited to the following domain:

{domain}

STRICT RULES:
- Answer ONLY questions related to this domain.
- If the question is outside this domain, respond EXACTLY with:
"Sorry, I don’t know about this question. Please ask something related to the selected module."

Conversation History:
{{history}}

User Question:
{{question}}

Answer:
"""
    )

    # ---------------------------------
    # LLM Setup
    # ---------------------------------
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.3
    )

    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=st.session_state.memory
    )

    # ---------------------------------
    # User Input
    # ---------------------------------
    user_question = st.text_input("💬 Your Question")

    if st.button("Submit") and user_question.strip():
        response = chain.run(question=user_question)

        st.session_state.chat_history.append(("User", user_question))
        st.session_state.chat_history.append(("AI", response))

    # ---------------------------------
    # Display Conversation
    # ---------------------------------
    st.markdown("### 📖 Conversation History")

    for role, msg in st.session_state.chat_history:
        if role == "User":
            st.markdown(f"**🧑 User:** {msg}")
        else:
            st.markdown(f"**🤖 AI Mentor:** {msg}")

    # ---------------------------------
    # Download Conversation (MANDATORY)
    # ---------------------------------
    if st.session_state.chat_history:
        conversation_text = ""
        for role, msg in st.session_state.chat_history:
            conversation_text += f"{role}: {msg}\n\n"

        file_name = f"{module}_Chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        st.download_button(
            label="📥 Download Conversation",
            data=conversation_text,
            file_name=file_name,
            mime="text/plain"
        )

    # ---------------------------------
    # Reset / Change Module
    # ---------------------------------
    st.markdown("---")
    if st.button("🔄 Change Module / Restart"):
        st.session_state.selected_module = None
        st.session_state.chat_history = []
        st.session_state.memory = ConversationBufferMemory(
            memory_key="history",
            return_messages=True
        )
        st.rerun()
