import asyncio
import time
from typing import Any, Dict


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


class AsyncScheduler:
    def __init__(self, run_interval: float = 0.1):
        self.run_interval = run_interval
        self.tasks: Dict[str, Dict[str, Any]] = {}
        self.is_running = False

    def add_task(self, target: Task, args: tuple = (), kwargs: dict = None):
        self.tasks[target.name] = {
            "target": target,
            "args": args,
            "kwargs": kwargs or {},
        }

    def get_task(self, name: str) -> Task:
        return self.tasks[name]["target"]

    def stop_task(self, name: str):
        self.get_task(name).stop()

    def start_task(self, name: str):
        self.get_task(name).start()

    def update_task_interval(self, name: str, interval: float):
        self.get_task(name).interval = interval

    async def run(self):
        self.is_running = True
        while self.is_running:
            current_time = time.time()
            for task_name, task_info in self.tasks.items():
                target: Task = task_info["target"]
                if target.should_invoke(current_time):
                    await target.execute(*task_info["args"], **task_info["kwargs"])
            await asyncio.sleep(self.run_interval)
