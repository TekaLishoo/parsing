import asyncio
from fastapi import FastAPI
from routers import lamoda_router, twitch_router
from parsing_scripts.lamoda_parser import LamodaParser
from parsing_scripts.twitch_parser import TwitchParser
import asyncio
import os
from fastapi_pagination import Page, add_pagination
from parsing_scripts.run_parser import run
from kq import Queue
from kafka import KafkaProducer
from json import dumps

app = FastAPI()
app.include_router(lamoda_router.router)
app.include_router(twitch_router.router)


@app.get('/parsing')
async def parsing():
    await run()

add_pagination(app)
