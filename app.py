import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os

st.set_page_config(page_title="Agente HIPAA", page_icon="📄")
st.title("Agente de consulta sobre HIPAA")

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

@st.cache_resource
def cargar_cadena():
    loader = PyPDFLoader("hippa.pdf")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    vectorstore = InMemoryVectorStore.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.2)
    prompt = ChatPromptTemplate.from_template(
        """Responde siempre en español, de forma clara y profesional, usando solo el contexto.
Contexto: {context}
Pregunta: {question}
Respuesta:"""
    )
    def format_docs(d):
        return "\n\n".join(x.page_content for x in d)
    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt | llm | StrOutputParser()
    )

rag_chain = cargar_cadena()

pregunta = st.text_input("Escribe tu pregunta sobre HIPAA:")
if pregunta:
    with st.spinner("Buscando en el documento..."):
        respuesta = rag_chain.invoke(pregunta)
    st.write(respuesta)
