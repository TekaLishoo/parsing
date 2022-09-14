from fastapi import APIRouter, Depends
from schemas.lamoda_schema import ProductSchema
from fastapi_pagination import Page
from dao.container_mongo import ContainerMongo


router = APIRouter(
    prefix="/lamoda",
    tags=[
        "lamoda",
    ],
)


@router.get("/", response_model=Page[ProductSchema])
def get_products(mongo=Depends(ContainerMongo)):
    """
    Return all lamoda products in a database
    """
    return mongo.get_list_lamoda_products()


@router.get("/id/{id}")
def one_prod(id: str, mongo=Depends(ContainerMongo)):
    """
    Return a product with a given id
    """
    return mongo.get_by_id(id)


@router.get("/{brand}", response_model=Page[ProductSchema])
def prods_by_brand(brand: str, mongo=Depends(ContainerMongo)):
    """
    Return all products of a particular brand.
    """
    return mongo.get_lamoda_brand(brand)
