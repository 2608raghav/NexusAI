from fastapi import FastAPI

from .service import FinanceService
from .agent_card import agent_card
from .executor import FinanceAgentExecutor

from a2a.server.request_handlers import DefaultRequestHandlerV2
from a2a.server.routes import (
    add_a2a_routes_to_fastapi,
    create_agent_card_routes,
    create_jsonrpc_routes,
)
from a2a.server.tasks import InMemoryTaskStore


app = FastAPI(title="Finance Agent")

service = FinanceService()
executor = FinanceAgentExecutor()
task_store = InMemoryTaskStore()

request_handler = DefaultRequestHandlerV2(
    agent_executor=executor,
    task_store=task_store,
    agent_card=agent_card,
)

a2a_jsonrpc_routes = create_jsonrpc_routes(
    request_handler,
    rpc_url="/a2a"
)

a2a_agent_card_routes = create_agent_card_routes(
    agent_card
)

add_a2a_routes_to_fastapi(
    app,
    jsonrpc_routes=a2a_jsonrpc_routes,
    agent_card_routes=a2a_agent_card_routes,
)


@app.get("/")
def root():
    return {"message": "Finance Agent is running"}


@app.get("/stock")
def get_stock(symbol: str):
    return service.get_stock_price(symbol)