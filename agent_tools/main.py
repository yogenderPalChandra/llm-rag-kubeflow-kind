from agent_executor import setup_agent

if __name__ == "__main__":
    agent = setup_agent()
    while True:
        q = input("Ask the agent a question (or 'exit'): ")
        if q.lower() == "exit":
            break
        print(agent.run(q))
