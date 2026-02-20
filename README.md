# 🎓 EduIntel AI  
### Enterprise Academic Knowledge Platform (RAG-Based System)

EduIntel AI is an enterprise-grade Retrieval-Augmented Generation (RAG) system designed for academic institutions.  
It enables intelligent querying over structured institutional data such as admissions, academics, hostel, and placements using semantic search and LLM integration.

This project demonstrates real-world implementation of a modular AI-powered knowledge retrieval system.

---

## 🚀 Key Features

- 🔎 Semantic Search using FAISS vector database
- 🧠 Sentence-Transformers for text embeddings
- 📄 Multi-format document ingestion (PDF, DOCX, CSV, TXT)
- 🏫 Enterprise-level folder architecture
- 🔐 Role-Based Access Control
- 💬 Streamlit-based interactive UI
- ⚡ OpenRouter LLM API integration
- 🧩 Modular and scalable code structure

---

## 🏗️ Project Structure

```
Academic_Rag_Chatbot/
│
├── __pycache__/
├── enterprise_data/
│   ├── Admissions/
│   │   └── ... (files inside Admissions)
│   ├── Academics/
│   │   └── ... (files inside Academics)
│   ├── Hostel/
│   │   └── ... (files inside Hostel)
│   └── Placements/
│       └── ... (files inside Placements)
│
├── venv/
│   └── ... (virtual environment files)
│
├── .gitattributes
├── app.py
├── config.py
├── vector_store.py
├── document_loader.py
├── rag_engine.py
├── ui_components.py
├── README.md
└── requirements.txt
```

---

## 📦 Module Descriptions

### 1️⃣ app.py
Main Streamlit application file.  
- Handles user interface  
- Accepts user queries  
- Displays chatbot responses  
- Connects retrieval system with LLM  

---

### 2️⃣ config.py
Configuration management module.  
- Stores API keys  
- Defines model settings  
- Controls environment configurations  

---

### 3️⃣ document_loader.py
Document ingestion module.  
- Loads documents from enterprise_data folders  
- Supports PDF, DOCX, CSV, TXT formats  
- Cleans and preprocesses text  

---

### 4️⃣ vector_store.py
Vector database management module.  
- Converts text into embeddings  
- Stores embeddings in FAISS  
- Performs similarity search for query retrieval  

---

### 5️⃣ enterprise_data/
Structured data directory representing institutional departments:  
- Admissions  
- Academics  
- Hostel  
- Placements  

Simulates real-world enterprise knowledge segmentation.

---

### 6️⃣ requirements.txt
Dependency management file containing all required Python libraries.

---

## ⚙️ How It Works

1. Documents are loaded from enterprise_data folders.
2. Text is converted into embeddings using Sentence-Transformers.
3. Embeddings are stored in FAISS vector database.
4. User query is converted into embedding.
5. Relevant context is retrieved using semantic similarity.
6. Context is passed to LLM via OpenRouter API.
7. Final response is generated and displayed in Streamlit UI.

---

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit
- FAISS
- Sentence-Transformers
- OpenRouter API
- Modular OOP Design

---

## ▶️ Installation & Running the Application

```bash
git clone https://github.com/sandhya-sp137/Academic-Rag-Chatbot.git
cd Academic-RAG-Chatbot
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎯 Use Cases

- Academic institution AI assistant
- Enterprise document intelligence
- Knowledge management system
- GenAI portfolio project
- RAG architecture demonstration

---

## 📌 Highlights

✔ Enterprise-level folder structure  
✔ Real-world RAG implementation  
✔ Clean modular architecture  
✔ Scalable and production-ready design  

---

## 👨‍💻 Author

Developed as an Enterprise AI Portfolio Project to demonstrate practical implementation of Retrieval-Augmented Generation (RAG) systems.

---

## ⭐ If You Like This Project


Give it a star on GitHub and connect with me!

