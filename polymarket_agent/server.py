import asyncio
import time

from fastapi import FastAPI

from polymarket_agent.engine import AsyncScheduler, Task


class FirstTask(Task):
    async def ainvoke(self, message: str):
        print(f"[{time.strftime('%H:%M:%S')}] first task ainvoke: {message}")


class SecondTask(Task):
    def invoke(self, message: str):
        print(f"[{time.strftime('%H:%M:%S')}] second task invoke: {message}")


app = FastAPI()
scheduler = AsyncScheduler()


@app.on_event("startup")
async def startup_event():
    # Add tasks to the scheduler
    first = FirstTask(name="Database", interval=2.0)
    second = SecondTask(name="Heartbeat", interval=5.0)

    scheduler.add_task(first, args=("ProductionDB",))
    scheduler.add_task(second, args=("Heartbeat",))

    # Run the scheduler in the background
    asyncio.create_task(scheduler.run())


@app.get("/tasks")
def get_tasks():
    return {
        name: {
            "is_enabled": task_info["target"].enabled,
            "interval": task_info["target"].interval,
            "last_run": task_info["target"].last_run,
        }
        for name, task_info in scheduler.tasks.items()
    }


@app.get("/tasks/{task_name}")
def get_task(task_name: str):
    task = scheduler.get_task(task_name)
    return {
        "name": task.name,
        "is_enabled": task.enabled,
        "interval": task.interval,
        "last_run": task.last_run,
    }


@app.post("/tasks/{task_name}/stop")
def stop_task(task_name: str):
    scheduler.stop_task(task_name)
    return {"message": f"Task {task_name} stopped"}


@app.post("/tasks/{task_name}/start")
def start_task(task_name: str):
    scheduler.start_task(task_name)
    return {"message": f"Task {task_name} started"}


@app.post("/tasks/{task_name}/interval")
def update_interval(task_name: str, interval: float):
    scheduler.update_task_interval(task_name, interval)
    return {"message": f"Task {task_name} interval updated to {interval}"}
