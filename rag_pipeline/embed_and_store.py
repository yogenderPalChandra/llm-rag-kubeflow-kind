from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def create_vectorstore(chunks, persist_dir="db"):
    embeddings = OllamaEmbeddings(model="llama3")
    vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=persist_dir)
    vectordb.persist()
    return vectordb
