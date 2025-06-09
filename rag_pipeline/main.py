from load_docs import load_and_split
from embed_and_store import create_vectorstore
from query_engine import run_query

if __name__ == "__main__":
    # Load your document
    chunks = load_and_split("data/test.txt")

    # Create or load vector database
    create_vectorstore(chunks)

    # Ask something!
    while True:
        query = input("Ask a question (or 'exit'): ")
        if query.lower() == "exit":
            break
        answer = run_query(query)
        print("Answer:", answer)
