from fastapi_pagination.ext.pymongo import paginate
from db.get_database import Mongo
from di.controller_general import ControllerGeneral
from config.config import Settings
from kafka import KafkaConsumer
from fastapi import HTTPException


class ContainerMongo:
    """
    Returns an object of Mongo database with required user, password and requested database.
    """

    general_settings = ControllerGeneral(Settings())

    def __init__(self):
        self.mongo = Mongo(
            self.general_settings.mongo_user,
            self.general_settings.mongo_password,
            self.general_settings.mongo_db,
        )

    async def send_lamoda_data(self, consumer: KafkaConsumer):
        products = self.mongo.client.products
        products_insert = []
        for message in consumer:
            products_insert.append(message.value)
        products.insert_many(products_insert)
        print(f"{len(products_insert)} products inserted!")

    async def send_twitch_data(self, consumer: KafkaConsumer):
        streams = self.mongo.client.streams
        streams_insert = []
        for message in consumer:
            streams_insert.append(message.value)
        streams.insert_many(streams_insert)
        print(f"{len(streams_insert)} products inserted!")

    def db_exception(self, message: str):
        raise HTTPException(status_code=404, detail=message)

    def get_list_lamoda_products(self):
        products = self.mongo.client.products
        if products.estimated_document_count() == 0:
            self.db_exception(
                "There are no products in a database. Please run a parsing firstly."
            )
        return paginate(products)

    def get_list_twitch_streams(self):
        streams = self.mongo.client.streams
        if streams.estimated_document_count() == 0:
            self.db_exception(
                "There are no products in a database. Please run a parsing firstly."
            )
        return paginate(streams)
