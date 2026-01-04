from typing import Any

from polymarket_agent.engine.task import Task


class Agent(Task):
    async def execute(self, *args: Any, **kwargs: Any) -> None:
        print("Agent task is executing...")
