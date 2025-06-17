from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.llms import Ollama
from .calculator import calculator
import os

def setup_agent():
    tools = [
        Tool(
            name="Calculator",
            func=calculator,
            description="Useful for math problems. Input must be a valid arithmetic expression."
        )
    ]
    llm = Ollama(model="llama3", base_url=os.getenv("OLLAMA_HOST"))
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    return agent
