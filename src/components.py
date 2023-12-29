from helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
import replicate
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers,OpenAI
from langchain.chains import RetrievalQA,LLMChain
from dotenv import load_dotenv
from prompt import *
import os
# import google.generativeai as genai
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)
index_name="mchatbot"
