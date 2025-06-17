from flask import Flask, request, jsonify
from agent_tools.agent_executor import setup_agent
from rag_pipeline.load_docs import load_and_split
from rag_pipeline.embed_and_store import create_vectorstore
import os

PERSIST_DIR = "rag_pipeline/db"
DOC_PATH = "rag_pipeline/data/test.txt"

# Bootstrap vector DB
def bootstrap_vector_db():
    os.makedirs("rag_pipeline/data", exist_ok=True)
    if not os.path.exists(PERSIST_DIR):
        print("[INFO] Bootstrapping vector DB...")
        chunks = load_and_split(DOC_PATH)
        create_vectorstore(chunks, persist_dir=PERSIST_DIR)

# Initialize agent and Flask app
bootstrap_vector_db()
agent = setup_agent()
app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' field"}), 400

    question = data["question"]
    answer = agent.run(question)
    return jsonify({"question": question, "answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
