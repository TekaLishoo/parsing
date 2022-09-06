from fastapi import APIRouter
from fastapi_pagination import Page, add_pagination, paginate

router = APIRouter(prefix='/twitch', tags=['twitch', ])


@router.get('/')
def list_of_objs():
    """
    Return all twitch objects in a database
    """
    return {'message': 'A list of objects'}


@router.get('/{id}')
def one_obj(id: int):
    """
    Return an object with a given id
    """
    return {'message': f'An object with id {id}'}
