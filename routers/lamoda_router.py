from fastapi import APIRouter, Depends
from schemas.lamoda_schema import ProductSchema
from fastapi_pagination import Page
from dao.container_mongo import ContainerMongo


router = APIRouter(prefix='/lamoda', tags=['lamoda', ])


@router.get('/', response_model=Page[ProductSchema])
def get_products(mongo=Depends(ContainerMongo)):
    """
    Return all lamoda products in a database
    """
    return mongo.get_list_lamoda_products()


@router.get('/{category}')
def prods_by_category(category: str):
    """
    Return all products in a particular category
    """
    return {'message': f'A list of products in the category {category}'}


@router.get('/{id}')
def one_prod(id: int):
    """
    Return a product with a given id
    """
    return {'message': f'A product with id {id}'}


