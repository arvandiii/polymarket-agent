from typing import Any

from polymarket_agent.engine.task import Task
from polymarket_agent.utils.logger import get_logger


class Trader(Task):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.logger = get_logger(__name__)

    async def ainvoke(self, *args: Any, **kwargs: Any) -> None:
        self.logger.info("Trader task is executing...")
