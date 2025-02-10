import os
import torch
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_community.vectorstores import FAISS
from utils import read_and_format_cocktails, form_prompt
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from config import CSV_PATH, HUGGINGFACE_EMBEDDINGS_MODEL_NAME, OPEN_SOURCE_MODEL_NAME, USE_API

embedding_model = HuggingFaceEmbeddings(model_name=HUGGINGFACE_EMBEDDINGS_MODEL_NAME)
texts = read_and_format_cocktails(CSV_PATH)
vector_store = FAISS.from_texts(texts, embedding_model)
if USE_API:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=OPENAI_API_KEY,
        max_tokens=100
    )
else:
    tokenizer = AutoTokenizer.from_pretrained(OPEN_SOURCE_MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        OPEN_SOURCE_MODEL_NAME,
        device_map="auto",
        torch_dtype=torch.float16
    )
    pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=1024, max_new_tokens=100, return_full_text=False)
    llm = HuggingFacePipeline(pipeline=pipeline)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load HTML templates
templates = Jinja2Templates(directory="templates")

class QueryModel(BaseModel):
    query: str

@app.post("/query/")
async def query_rag(data: QueryModel):
    """Retrieves relevant documents and generates a response."""
    query = data.query
    retrieved_docs = vector_store.similarity_search(query, k=10)
    retrieved_text = "\n\n".join([doc.page_content for doc in retrieved_docs])
    prompt = form_prompt(query, retrieved_text)
    if USE_API:
        response = llm.invoke(prompt).content

    else:
        response = llm.invoke(prompt)
    return {"response": response, "context": retrieved_text}

@app.get("/", response_class=HTMLResponse)
async def serve_frontend(request: Request):
    """Serve the frontend HTML."""
    return templates.TemplateResponse("index.html", {"request": request})
