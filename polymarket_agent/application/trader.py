from typing import Any

from polymarket_agent.engine.task import Task


class Trader(Task):
    async def execute(self, *args: Any, **kwargs: Any) -> None:
        print("Trader task is executing...")
