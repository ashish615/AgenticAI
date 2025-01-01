from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.ollama import Ollama

agent = Agent(
    model=Ollama(id="llama3.2"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=[
        "Use tables to display data.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA. Show in tables.", stream=True
)
