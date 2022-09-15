from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from schemas.twitch_schema import StreamSchema
from dao.container_mongo import ContainerMongo
from fastapi_redis_cache import cache
from fastapi.encoders import jsonable_encoder


router = APIRouter(
    prefix="/twitch",
    tags=[
        "twitch",
    ],
)


@router.get("/", response_model=Page[StreamSchema])
@cache()
def list_of_objs(mongo=Depends(ContainerMongo)):
    """
    Return all twitch objects in a database
    """
    return mongo.get_list_twitch_streams()


@router.get("/id/{id}")
@cache()
def one_obj(id: str, mongo=Depends(ContainerMongo)):
    """
    Return an object with a given id
    """
    return mongo.get_by_id(id)
