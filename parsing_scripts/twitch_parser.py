from parsing_scripts.base_parser import AbstractParser
from kafka import KafkaConsumer, KafkaProducer
import asyncio


class TwitchParser(AbstractParser):
    BASE_URL = "https://api.twitch.tv/helix/streams"

    async def parse(self, producer: KafkaProducer):
        soup = await self.get_soup(self.BASE_URL)
        for i in range(10):
            d = producer.send('topic_twitch', value={'counter': 'twitch'})
            data = d.get()
            print(f'send {data}')
            await asyncio.sleep(1)

