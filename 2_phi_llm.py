from phi.agent import Agent
from phi.model.ollama import Ollama
agent = Agent(
    model=Ollama(id="llama3.2"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Write a love story between a tomato and a chili",stream=True)
