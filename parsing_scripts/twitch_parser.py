from parsing_scripts.base_parser import AbstractParser
from dao.container_kafka import Kafka
from dao.container_mongo import ContainerMongo


class TwitchParser(AbstractParser):
    """
    Parsing Twitch API site.
    Sends data to kafka.
    """

    BASE_URL = "https://api.twitch.tv/helix/streams"
    AUTH_URL = "https://id.twitch.tv/oauth2/token"

    def __init__(self, kafka: Kafka, mongo: ContainerMongo):
        self.kafka = kafka
        self.mongo = mongo

    async def parse(self):

        data = self.auth(self.AUTH_URL, self.BASE_URL)
        for stream in data.json()["data"]:
            stream_data = {
                "user_login": stream["user_login"],
                "game_name": stream["game_name"],
                "type": stream["type"],
                "title": stream["title"],
                "viewer_count": stream["viewer_count"],
                "language": stream["language"],
                "is_mature": stream["is_mature"],
            }
            self.kafka.producer.send("topic_twitch", value=stream_data)
            print(f"send {stream_data}")

        await self.mongo.send_twitch_data(self.kafka.consumer_twitch)
