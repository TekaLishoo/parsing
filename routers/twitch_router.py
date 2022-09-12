from fastapi import APIRouter
from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.pymongo import paginate
from schemas.twitch_schema import StreamSchema
from db.get_database import Mongo
import os


router = APIRouter(prefix='/twitch', tags=['twitch', ])


@router.get('/', response_model=Page[StreamSchema])
def list_of_objs():
    """
    Return all twitch objects in a database
    """
    client = Mongo(os.environ['MONGO_USER'], os.environ['MONGO_PASS'], os.environ['MONGO_DB'])
    streams = client().streams
    return paginate(streams)


@router.get('/{id}')
def one_obj(id: int):
    """
    Return an object with a given id
    """
    return {'message': f'An object with id {id}'}
