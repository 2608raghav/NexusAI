from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.types import Message, Part, Role

from .service import FinanceService


class FinanceAgentExecutor(AgentExecutor):

    def __init__(self):
        self.finance_service = FinanceService()

    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue
    ) -> None:

        print("A2A Finance Agent received a request")

        user_input = context.get_user_input()

        print("User input:", user_input)

        # Simple symbol extraction for now
        symbol = user_input.strip().upper()

        result = self.finance_service.get_stock_price(symbol)

        if "price" in result:
            response_text = (
                f"{result['symbol']} current price is "
                f"${result['price']}"
            )
        else:
            response_text = result.get(
                "error",
                "Could not retrieve stock price"
            )

        message = Message(
            message_id="finance-response-1",
            role=Role.ROLE_AGENT,
            parts=[
                Part(
                    text=response_text
                )
            ]
        )

        await event_queue.enqueue_event(message)

    async def cancel(
        self,
        context: RequestContext,
        event_queue: EventQueue
    ) -> None:

        print("A2A Finance Agent task cancelled")