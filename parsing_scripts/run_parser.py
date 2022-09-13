import asyncio
from parsing_scripts.lamoda_parser import LamodaParser
from parsing_scripts.twitch_parser import TwitchParser
from dao.container_kafka import Kafka
from dao.container_mongo import ContainerMongo


async def run():
    asyncio.get_event_loop()
    kafka = Kafka()
    mongo = ContainerMongo()
    tasks = [
        asyncio.create_task(LamodaParser(kafka, mongo).parse()),
        asyncio.create_task(TwitchParser(kafka, mongo).parse()),
    ]
    asyncio.gather(*tasks)

