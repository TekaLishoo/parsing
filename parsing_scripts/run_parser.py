import asyncio
from parsing_scripts.lamoda_parser import LamodaParser
from parsing_scripts.twitch_parser import TwitchParser
from dao.container_kafka import Kafka
from dao.container_mongo import ContainerMongo


async def run():
    asyncio.get_event_loop()
    k = Kafka()
    mongo = ContainerMongo()
    tasks = [
        asyncio.create_task(LamodaParser().parse(k, mongo)),
        asyncio.create_task(TwitchParser().parse(k, mongo)),
    ]
    asyncio.gather(*tasks)

