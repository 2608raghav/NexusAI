from a2a.types import AgentCard, AgentSkill


finance_skill = AgentSkill(
    id="stock_price",
    name="Stock Price",
    description="Provides the current stock price for a given stock symbol.",
    tags=[
        "finance",
        "stocks",
        "stock price"
    ],
    examples=[
        "What is the current price of AAPL?",
        "Give me the stock price of MSFT"
    ]
)


agent_card = AgentCard(
    name="NexusAI Finance Agent",
    description="An agent that provides current stock prices.",
    url="http://127.0.0.1:8004",
    version="1.0.0",
    protocol_version="1.0",
    skills=[
        finance_skill
    ]
)