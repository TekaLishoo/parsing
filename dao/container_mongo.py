import asyncio
from fastapi_pagination.ext.pymongo import paginate
from db.get_database import Mongo
from di.controller_general import ControllerGeneral
from config.config import Settings
from kafka import KafkaConsumer


class ContainerMongo:
    """
    Returns an object of Mongo database with required user, password and requested database.
    """
    general_settings = ControllerGeneral(Settings())

    def __init__(self):
        self.mongo = Mongo(
            self.general_settings.mongo_user,
            self.general_settings.mongo_password,
            self.general_settings.mongo_db
        )

    async def send_lamoda_data(self, consumer: KafkaConsumer):
        products = self.mongo.client.products
        products_insert = []
        for message in consumer:
            products_insert.append(message.value)
        products.insert_many(products_insert)
        print(f'{len(products_insert)} products inserted!')


    async def send_twitch_data(self):
        pass

    def get_list_lamoda_products(self):
        products = self.mongo.client.products
        print(products)
        return paginate(products)
