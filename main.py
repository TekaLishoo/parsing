from routers import lamoda_router, twitch_router
from fastapi_pagination import add_pagination
from parsing_scripts.run_parser import run
from dao.container_redis import RedisCash
from fastapi import FastAPI

app = FastAPI()
app.include_router(lamoda_router.router)
app.include_router(twitch_router.router)


@app.on_event("startup")
def startup():
    RedisCash()


@app.get("/parsing")
async def parsing():
    await run()


add_pagination(app)
