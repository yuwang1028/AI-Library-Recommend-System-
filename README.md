# 📚 AI Library Chatbot

An AI-powered **book recommendation chatbot** using **FastAPI, LangChain, Open Library API, and OpenAI's GPT models**.  
It understands user queries, **extracts intent (genre, themes, or author preferences)**, and returns personalized book suggestions.
![Screenshot 2025-02-16 at 21 41 03](https://github.com/user-attachments/assets/7df2bc75-a1e1-4d2b-b142-dfd608bf0271)
![Screenshot 2025-02-16 at 21 42 28](https://github.com/user-attachments/assets/f0506178-0bdb-405f-a55a-40be3dc4ecd5)

---

## 🤖 **How the AI Agent Works**
This project features a **multi-agent AI system** consisting of:
1. **Natural Language Processing (NLP) Agent**  
   - **Extracts intent** from user queries (genre, author, themes).  
   - Uses **OpenAI GPT-4** to interpret input.  
   - Example:  
     **User:** "I want a book like Harry Potter"  
     **AI Extracts:** `Genre: Fantasy, Theme: Magic, Young Adult`

2. **Recommendation Agent**  
   - Fetches books **matching user intent** from **Open Library API**.  
   - Uses **FAISS vector embeddings** to find similar books.  
   - Returns **book recommendations** with title, author, and description.

### **🛠 AI Workflow**
1. **User inputs query** (e.g., `"I want a mystery novel"`).
2. **NLP Agent processes input** → Extracts key **genre & theme**.
3. **Recommendation Agent fetches books** from Open Library API.
4. **Response is returned** to the frontend.

---

## 🎯 **Features**
✅ AI-powered **book recommendations**  
✅ **Natural Language Understanding** with OpenAI GPT-4  
✅ Fetches books from **Open Library API**  
✅ **Vector search with FAISS** for similar books  
✅ Modern **Bootstrap-styled frontend**  
✅ Deployed on **GitHub Pages (Frontend) & Render (Backend)**  ---

## 🛠 **Tech Stack**
- **Backend**: FastAPI, LangChain, OpenAI, Open Library API  
- **Frontend**: HTML, Bootstrap, JavaScript  
- **Deployment**: GitHub Pages (Frontend), Render (Backend)  

---
## 🚀 **How to Start the Project**
This guide walks you through **setting up and running** the AI Library Chatbot on your **local machine**.

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-github-username/ai-library-chatbot.git
cd ai-library-chatbot
```

### **2️⃣Setup & Run the Backend (FastAPI)
```sh

python -m venv langchain_env
source langchain_env/bin/activate  # macOS/Linux
langchain_env\Scripts\activate     # Windows

pip install -r requirements.txt

OPENAI_API_KEY=your_openai_api_key_here

uvicorn app:app --reload
```
### **3️⃣ Setup & Run the Frontend
```
python -m http.server 8080
```


