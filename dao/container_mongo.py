from db.get_database import Mongo
from di.controller_general import ControllerGeneral
from config.config import Settings


general_settings = ControllerGeneral(Settings())


class ContainerMongo:
    """
    Returns an object of Mongo database with required user, password and requested database.
    """

    def __init__(self):
        self.mongo = Mongo(
            general_settings.mongo_user,
            general_settings.mongo_password,
            general_settings.mongo_db
        )
