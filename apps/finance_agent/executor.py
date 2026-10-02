from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.types import Message, Part, Role


class FinanceAgentExecutor(AgentExecutor):

    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue
    ) -> None:

        print("A2A Finance Agent received a request")

        message = Message(
            message_id="finance-response-1",
            role=Role.ROLE_AGENT,
            parts=[
                Part(
                    text="Finance Agent A2A request received"
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