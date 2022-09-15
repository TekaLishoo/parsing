from config.config import Settings


class ControllerGeneral:
    def __init__(self, actual_settings: Settings):
        self.mongo_user = actual_settings.MONGO_USER
        self.mongo_password = actual_settings.MONGO_PASS
        self.mongo_db = actual_settings.MONGO_DB

        self.client_id = actual_settings.TWITCH_CLIENT_ID
        self.secret_key = actual_settings.TWITCH_SECRET_KEY

        self.redis_url = actual_settings.REDIS_URL
