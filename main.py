from agent_tools.agent_executor import setup_agent
from rag_pipeline.load_docs import load_and_split
from rag_pipeline.embed_and_store import create_vectorstore
import os

PERSIST_DIR = "rag_pipeline/db"
DOC_PATH = "rag_pipeline/data/test.txt"

def bootstrap_vector_db():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(PERSIST_DIR):
        print("[INFO] Bootstrapping vector DB...")
        chunks = load_and_split(DOC_PATH)
        create_vectorstore(chunks, persist_dir=PERSIST_DIR)

if __name__ == "__main__":
    bootstrap_vector_db()
    agent = setup_agent()

    while True:
        query = input("Ask a question (or 'exit'): ")
        if query.lower() == "exit":
            break
        answer = agent.run(query)
        print("Answer:", answer)
