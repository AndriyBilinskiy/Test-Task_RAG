# **🍸 Cocktail AI RAG App**
This is a **Retrieval-Augmented Generation (RAG) app** that helps users explore cocktail recipes. The app allows users to ask cocktail-related questions, retrieves relevant cocktail data from a **FAISS vector database**, and generates AI-powered responses.

## **🚀 Features**
✅ **Retrieval-Augmented Generation (RAG)** – Uses FAISS to search for relevant cocktail data before generating responses.  
✅ **Uses OpenAI GPT-3.5 or opensource GPT-2** – Provides intelligent, human-like answers.  
✅ **FastAPI Backend** – A lightweight and efficient API.  
✅ **Interactive Web UI** – Simple HTML + JavaScript frontend for easy access.
---

## **📌 Project Structure**
```
/cocktail-ai-app
│── /templates                # HTML frontend
│   ├── index.html            # User interface
│── /utils.py                 # Functions for reading & formatting cocktail data
│── /config
│   ├── config.py             # Configuration variables (e.g., model names, paths)
│── faiss_index/              # Saved FAISS vector database
│── app.py                # FastAPI backend
│── requirements.txt          # Required dependencies
│── README.md                 # Documentation
```

---

### **2️⃣ Create & Activate Virtual Environment**
#### **On macOS/Linux**
```sh
python3 -m venv venv
source venv/bin/activate
```
#### **On Windows**
```sh
python -m venv venv
venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## **Using OpenAi API**
By default the app uses GPT-2 model, if you want to use GPT-3.5 you need to set your OpenAI API key and also set 
```USE_API = True``` in ```config.py```.

Set your API key as an **environment variable**:

#### **On macOS/Linux**
```sh
export OPENAI_API_KEY="your-api-key-here"
```
#### **On Windows (Command Prompt)**
```sh
set OPENAI_API_KEY=your-api-key-here
```
#### **On Windows (PowerShell)**
```sh
$env:OPENAI_API_KEY="your-api-key-here"
```

---

## **🚀 Running the App**
### **1️⃣ Start the FastAPI Server**
```sh
uvicorn rag_app:app --host 0.0.0.0 --port 8000 --reload
```

### **2️⃣ Open the Web Interface**
1. Open your browser and go to:  
   **📌 `http://127.0.0.1:8000/`**
2. Type a question like:  
   ❓ **"What are 5 cocktails containing lemon?"**  
3. Get an AI-powered response! 🎉

---

## **📡 API Endpoints**
### **1️⃣ Query Endpoint (`/query/`)**
**🔹 Method:** `POST`  
**🔹 Description:** Retrieves cocktail information using FAISS & OpenAI.  
**🔹 Request Example:**
```json
{
    "query": "What are 5 cocktails containing lemon?"
}
```
**🔹 Response Example:**
```json
{
    "response": "Here are 5 cocktails containing lemon: ...",
    "context": "Relevant cocktail descriptions..."
}
```

### **2️⃣ Web UI (`/`)**
**🔹 Method:** `GET`  
**🔹 Description:** Serves the frontend interface.

---

## **🔧 Configuration**
Edit **config.py** to modify settings like:
```python
CSV_PATH = "final_cocktails.csv"
HUGGINGFACE_EMBEDDINGS_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
USE_API = False
OPEN_SOURCE_MODEL_NAME = "gpt2"
```

---

### **🍸 Enjoy Your AI-Powered Cocktail Assistant! 🚀**