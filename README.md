# 🤖 AI Chatbot Mentor – Domain-Specific Intelligent Learning Assistant

AI Chatbot Mentor is a **domain-restricted, AI-powered mentoring application** designed to provide focused and distraction-free learning support across multiple technical domains.

Unlike generic chatbots, this system **strictly answers only within the selected module**, ensuring accurate, relevant, and reliable mentorship.

---

## 🚀 Features

- 🎯 **Module-Based Mentoring**
  - Python
  - SQL
  - Power BI
  - Exploratory Data Analysis (EDA)
  - Machine Learning (ML)
  - Deep Learning (DL)
  - Generative AI (Gen AI)
  - Agentic AI

- 🔒 **Strict Domain Control**
  - Questions outside the selected module are rejected with a fixed response
  - Prevents hallucinations and irrelevant answers

- 🧠 **Session-Based Conversation Memory**
  - Maintains full chat context during a session

- 📥 **Download Chat History (Key Highlight)**
  - Export complete conversation (User + AI)
  - Downloadable in `.txt` format
  - Useful for revision, notes, and portfolio documentation

- 🖥 **Clean & Interactive UI**
  - Built using Streamlit
  - Simple module selection and chat interface

---

## 🏗️ Tech Stack

| Component | Technology |
|--------|------------|
| Frontend | Streamlit |
| LLM Orchestration | LangChain |
| Language Model | OpenAI / Open-source (configurable) |
| Memory | ConversationBufferMemory |
| Export | Text (.txt) |

---

## 🧩 Architecture Overview

1. User selects a learning module  
2. A module-specific prompt is activated  
3. AI responds **only within that domain**  
4. Conversation history is stored in session memory  
5. User can download the full conversation anytime  

---

## 🖼️ Application Preview

![AI Chatbot Mentor UI](./assets/ui_preview.png)

---

## ⚙️ Installation & Setup

```bash
pip install -r requirements.txt
streamlit run app.py
