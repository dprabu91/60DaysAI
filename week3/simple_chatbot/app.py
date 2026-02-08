import os
import tempfile
import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --------------------------------------------------
# Load API key from .env
# --------------------------------------------------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("❌ OPENAI_API_KEY not found in .env file")
    st.stop()

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.set_page_config(page_title="PDF RAG Chatbot", layout="wide")
st.title("📄 Simple PDF RAG Chatbot (Python 3.13 SAFE)")
st.write("Upload a PDF and ask questions based on its content")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

# --------------------------------------------------
# Process PDF
# --------------------------------------------------
if uploaded_file:
    try:
        with st.spinner("Processing PDF..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                pdf_path = tmp.name

            loader = PyPDFLoader(pdf_path)
            documents = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.split_documents(documents)

            embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )

            vectorstore = FAISS.from_documents(chunks, embeddings)
            retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        st.success("✅ PDF processed successfully")

    except Exception as e:
        st.error("❌ Error processing PDF")
        st.exception(e)
        st.stop()

    finally:
        if "pdf_path" in locals() and os.path.exists(pdf_path):
            os.remove(pdf_path)

    # --------------------------------------------------
    # Question input
    # --------------------------------------------------
    query = st.text_input("Ask a question from the PDF")

    if query:
        try:
            llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0,
                api_key=OPENAI_API_KEY
            )

            prompt = ChatPromptTemplate.from_messages([
                ("system", "Answer using ONLY the context below:\n\n{context}"),
                ("human", "{question}")
            ])

            # -------------------------------
            # 🔥 PURE CORE RAG CHAIN 🔥
            # -------------------------------
            rag_chain = (
                {
                    "context": retriever,
                    "question": RunnablePassthrough()
                }
                | prompt
                | llm
                | StrOutputParser()
            )

            answer = rag_chain.invoke(query)

            st.subheader("📌 Answer")
            st.write(answer)

        except Exception as e:
            st.error("❌ Error generating answer")
            st.exception(e)
