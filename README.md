# Project Name - PrepAI 

### Table of Content :
[introduction](#introduction)
[How it Works](#Howitworks)
[Installation](#Installation)
[How to use  it](#HowtouseIt)

# Introduction
### PrepMate AI smart interview practice assistant
Prep AI is an intelligent interview preparation tool that helps job seekers practice effectively. By uploading a PDF with interview questions, users can interact with the app as if they were in a real interview. The system uses Retrieval-Augmented Generation (RAG) to provide meaningful, context-based answers and guidance.
# How it Works
1 Uploading the PDF The App 
it  extracts  text content  from each PDF

2 Text Chunking
The extracted text  is  Too large  to process at once 
The text  is splitted  into smaller, managable  chunks 
each chunk is stored  fr further processing

3. Embedding Creation (LLM)
A language Model (like Langchain-groq Embedding) converts text into a vectr Representation (a numeric  form that captures  sematic meaning)
These vectors are saved in  vector database memory
4 Retrival
when the user ask  a question , the query is also converted  into a vector usig the same  embedding
the system searches  for the most  semmatical similar chunks by comparing the query vector with stored text  vectors
The top matching  chunks are selected

5 Response Generation
The selected chunks are provided to a language model(llama 3.)
The model uses a  these chunks  as context to generate  a relevant  and accurate  response to the user question

# Installation 
1. clone the Repository
2. install the Required dependency
pip install -r requirements.txt
3. obtai the Groq API key from GROQ and add it to the .env file in the project directory

4. Usage
   Follow this steps
   1 Ensure that you have installed  the required Dependencies  and added the GROQ API key  to the .env file
   2  run  streamlit app.py
   3. The application willl launch on your Default browser ,Desplaying the usee interface
   4 Load  your pdf file
   

![s](https://github.com/user-attachments/assets/f4664bb8-13a4-4f6e-870a-ee0e3dac6ba1)
![s](https://github.com/user-attachments/assets/355f7123-e951-416b-89d5-626f3e25b48b)
![intervie](https://github.com/user-attachments/assets/1a2b1e85-a4f3-4aaa-9df8-eaef0eb06933)
