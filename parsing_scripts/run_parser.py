import asyncio
from parsing_scripts.lamoda_parser import LamodaParser
from parsing_scripts.twitch_parser import TwitchParser
from dao.container_kafka import Kafka


def run():
    asyncio.get_event_loop()
    k = Kafka()
    tasks = [
        asyncio.create_task(LamodaParser().parse(k.producer)),
        asyncio.create_task(TwitchParser().parse(k.producer)),
        asyncio.create_task(k.send_lamoda_data()),
        asyncio.create_task(k.send_twitch_data()),
    ]
    asyncio.gather(*tasks)

