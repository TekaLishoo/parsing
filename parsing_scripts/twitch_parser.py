from parsing_scripts.base_parser import AbstractParser
from dao.container_kafka import Kafka
from dao.container_mongo import ContainerMongo
import asyncio


class TwitchParser(AbstractParser):
    BASE_URL = "https://api.twitch.tv/helix/streams"

    def __init__(self, kafka: Kafka, mongo: ContainerMongo):
        self.kafka = kafka
        self.mongo = mongo

    async def parse(self):
        soup = await self.get_soup(self.BASE_URL)
        for i in range(10):
            d = self.kafka.producer.send('topic_twitch', value={'counter': 'twitch'})
            data = d.get()
            print(f'send {data}')
            await asyncio.sleep(1)

