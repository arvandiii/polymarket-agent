from polymarket_agent.application.agent import Agent
from polymarket_agent.application.trader import Trader
from polymarket_agent.engine.scheduler import AsyncScheduler


class Application:
    def __init__(self):
        self.scheduler = AsyncScheduler()
        self.trader = Trader(name="TraderTask", interval=1.0)
        self.agent = Agent(name="AgentTask", interval=2.0)
        self.scheduler.add_task(self.trader)
        self.scheduler.add_task(self.agent)

    async def start(self):
        await self.scheduler.run()

    def health(self):
        return {
            "status": "running" if self.scheduler.is_running else "stopped",
        }
