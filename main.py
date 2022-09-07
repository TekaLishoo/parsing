import asyncio
from fastapi import FastAPI
from routers import lamoda_router, twitch_router
from parsing_scripts.lamoda_parser import LamodaParser
from parsing_scripts.twitch_parser import TwitchParser
import asyncio
import os
from fastapi_pagination import Page, add_pagination

app = FastAPI()
app.include_router(lamoda_router.router)
app.include_router(twitch_router.router)


@app.on_event("startup")
async def startup_event():
    pass
    # lamoda_parser.lamoda_parser()
    # twitch_parser.twitch_parser()


@app.get('/parsing')
async def pars_lamoda():
    loop = asyncio.get_event_loop()
    tasks = [asyncio.create_task(LamodaParser().parse())]
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)

add_pagination(app)
