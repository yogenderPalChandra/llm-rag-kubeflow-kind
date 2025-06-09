from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma

def run_query(question, persist_dir="db"):
    vectordb = Chroma(persist_directory=persist_dir, embedding_function=None)
    retriever = vectordb.as_retriever()
    llm = Ollama(model="llama3")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(question)
