import time
from typing import Any


class Task:
    def __init__(self, name: str, interval: float = 1.0):
        self.name = name
        self.interval = interval
        self.last_run = 0.0
        self.enabled = True

    def should_invoke(self, current_time: float) -> bool:
        return self.enabled and current_time - self.last_run >= self.interval

    async def execute(self, *args: Any, **kwargs: Any):
        self.last_run = time.time()

        try:
            await self.ainvoke(*args, **kwargs)
        except NotImplementedError:
            self.invoke(*args, **kwargs)

    def invoke(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    async def ainvoke(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    def stop(self):
        self.enabled = False

    def start(self):
        self.enabled = True
