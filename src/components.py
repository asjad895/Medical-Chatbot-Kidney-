# from helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from langchain.embeddings import HuggingFaceEmbeddings
import replicate
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers,OpenAI
from langchain.chains import RetrievalQA,LLMChain
from dotenv import load_dotenv
# from prompt import *
import os
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("loading... embedding")
    return embeddings
# import google.generativeai as genai
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)
index_name="mchatbot"
