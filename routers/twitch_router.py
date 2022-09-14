from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from schemas.twitch_schema import StreamSchema
from dao.container_mongo import ContainerMongo


router = APIRouter(
    prefix="/twitch",
    tags=[
        "twitch",
    ],
)


@router.get("/", response_model=Page[StreamSchema])
def list_of_objs(mongo=Depends(ContainerMongo)):
    """
    Return all twitch objects in a database
    """
    return mongo.get_list_twitch_streams()


@router.get("/{id}")
def one_obj(id: int):
    """
    Return an object with a given id
    """
    return {"message": f"An object with id {id}"}
