from fastapi import FastAPI
from routers import lamoda_router, twitch_router
from fastapi_pagination import add_pagination
from parsing_scripts.run_parser import run
from dao.container_redis import ContainerRedisCash
from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache
import os

app = FastAPI()
app.include_router(lamoda_router.router)
app.include_router(twitch_router.router)


@app.on_event("startup")
def startup():
    ContainerRedisCash()


@app.get("/parsing")
async def parsing():
    await run()


add_pagination(app)
