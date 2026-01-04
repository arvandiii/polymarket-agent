import asyncio
from typing import Any, Dict

from polymarket_agent.engine.task import Task


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
            for _task_name, task_info in self.tasks.items():
                target: Task = task_info["target"]
                if target.should_invoke():
                    await target.execute(*task_info["args"], **task_info["kwargs"])
            await asyncio.sleep(self.run_interval)
