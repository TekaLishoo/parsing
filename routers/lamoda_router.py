from fastapi import APIRouter
from db.get_database import database
from schemas.lamoda_schema import ProductSchema
from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.pymongo import paginate

router = APIRouter(prefix='/lamoda', tags=['lamoda', ])


@router.get('/', response_model=Page[ProductSchema])
def get_products():
    """
    Return all lamoda products in a database
    """

    # example product - will be removed
    product = ProductSchema(
        category='home',
        brand='Zara',
        name='pillow',
        price=230.1,
        descroption={'color': 'red', 'material': 'cotton'}
    )
    products = database.products
    products.insert_one(product.dict())
    return paginate(products)


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


