from di.controller_general import ControllerGeneral
from config.config import Settings
from fastapi_redis_cache import FastApiRedisCache
from fastapi import Request, Response
from fastapi import APIRouter
from fastapi_pagination import Page


class ContainerRedisCash:
    """
    Redis object is for storing cache.
    """

    general_settings = ControllerGeneral(Settings())

    def __init__(self):
        redis_cache = FastApiRedisCache()
        redis_cache.init(
            host_url=self.general_settings.redis_url,
            prefix="parsing-cache",
            response_header="Parsing-Cache",
            ignore_arg_types=[Request, Response, APIRouter, Page]
        )
