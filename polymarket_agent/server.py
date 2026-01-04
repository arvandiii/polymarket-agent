import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from polymarket_agent.application.application import Application

application = Application()


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(application.start())
    yield


fast_api = FastAPI(lifespan=lifespan)


@fast_api.get("/health")
def health():
    return application.health()


if __name__ == "__main__":
    uvicorn.run(fast_api, host="0.0.0.0", port=8000)
