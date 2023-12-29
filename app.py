from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
import replicate
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers,OpenAI
from langchain.chains import RetrievalQA,LLMChain
from dotenv import load_dotenv
from src.prompt import *
from store_index import *
import os
# import google.generativeai as genai

app = Flask(__name__)

load_dotenv()
gemini_api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key = gemini_api_key)
replicate=os.environ.get('replicate')
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')


PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain_type_kwargs={"prompt": PROMPT}

# llm=CTransformers(model="../Model/llama-2-7b-chat.ggmlv3.q4_0.bin",
#                   model_type="llama",
#                   config={'max_new_tokens':512,
#                           'temperature':0.8})
# llm=model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("Who is the GOAT in the NBA?")
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
print("LLm Llama2-7b chat model...")


qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)



@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)

