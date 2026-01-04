import asyncio
import time
from typing import Any, Dict, List


class Task:
    def __init__(self, interval: float = 1.0):
        self.interval = interval
        self.last_run = 0.0

    def should_invoke(self, current_time: float) -> bool:
        return current_time - self.last_run >= self.interval

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


class AsyncScheduler:
    def __init__(self, run_interval: float = 0.1):
        self.run_interval = run_interval
        self.tasks: List[Dict[str, Any]] = []
        self.is_running = False

    def add_task(self, target: Task, args: tuple = (), kwargs: dict = None):
        self.tasks.append(
            {
                "target": target,
                "args": args,
                "kwargs": kwargs or {},
            }
        )

    async def run(self):
        self.is_running = True
        while self.is_running:
            current_time = time.time()
            for task in self.tasks:
                target: Task = task["target"]
                if target.should_invoke(current_time):
                    await target.execute(*task["args"], **task["kwargs"])
            await asyncio.sleep(self.run_interval)


class FirstTask(Task):
    async def ainvoke(self, message: str):
        print(f"[{time.strftime('%H:%M:%S')}] first task ainvoke: {message}")


class SecondTask(Task):
    def invoke(self, message: str):
        print(f"[{time.strftime('%H:%M:%S')}] second task invoke: {message}")


async def main():
    scheduler = AsyncScheduler()

    first = FirstTask(interval=2.0)
    second = SecondTask(interval=5.0)

    scheduler.add_task(first, args=("ProductionDB",))
    scheduler.add_task(second, args=("Heartbeat",))

    await scheduler.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
