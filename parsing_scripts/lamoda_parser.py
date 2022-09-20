from dao.container_kafka import Kafka
from parsing_scripts.base_parser import AbstractParser
from dao.container_mongo import ContainerMongo


class LamodaParser(AbstractParser):
    """
    Parsing LaModa site.
    Sends data to kafka.
    """

    BASE_URL = "https://lamoda.by"
    category_class = "x-footer-seo-menu-tab-links__item"
    product_class = "x-product-card__link"
    prod_category_class = "x-premium-product-title__model-name"
    prod_brand_class = "x-premium-product-title__brand-name"
    prod_price_class = "x-premium-product-prices__price"
    prod_description_attr_class = "x-premium-product-description-attribute__name"
    prod_description_value_class = "x-premium-product-description-attribute__value"

    def __init__(self, kafka: Kafka, mongo: ContainerMongo):
        self.kafka = kafka
        self.mongo = mongo

    async def parse(self):
        soup = await self.get_soup(self.BASE_URL)

        # find all links with product categories
        a_list = soup.find_all("a", attrs={"class": f"{self.category_class}"})

        # in case of one product can be in several categories we'll store visited product's links
        # to be sure not to visit one product twice
        visited_products = set()
        for a in a_list:
            actual_url = self.BASE_URL + a.attrs["href"]
            actual_soup = await self.get_soup(actual_url)

            # find all links with products
            actual_a_list = actual_soup.find_all(
                "a", attrs={"class": self.product_class}
            )
            for prod in actual_a_list:
                product_url = self.BASE_URL + prod.attrs["href"]
                if not (product_url in visited_products):
                    visited_products.add(product_url)

                    product_soup = await self.get_soup(product_url)
                    try:
                        name = product_soup.find(
                            "div", attrs={"class": self.prod_category_class}
                        ).get_text()
                        category = name.split()[0]
                    except AttributeError:
                        name = ""
                        category = ""
                    try:
                        brand = (
                            product_soup.find(
                                "span", attrs={"class": self.prod_brand_class}
                            )
                            .get_text()
                            .strip()
                        )
                    except AttributeError:
                        brand = ""
                    try:
                        price = (
                            product_soup.find(
                                "span", attrs={"class": self.prod_price_class}
                            )
                            .get_text()
                            .split()[0]
                        )
                    except AttributeError:
                        price = 0.0
                    description_attrs_list = product_soup.find_all(
                        "span", attrs={"class": self.prod_description_attr_class}
                    )
                    description_values_list = product_soup.find_all(
                        "span", attrs={"class": self.prod_description_value_class}
                    )

                    description = dict(
                        zip(
                            [attr.get_text() for attr in description_attrs_list],
                            [value.get_text() for value in description_values_list],
                        )
                    )

                    product_data = {
                        "category": category,
                        "brand": brand,
                        "name": name,
                        "price": price,
                        "description": description,
                    }

                    self.kafka.producer.send("topic_lamoda", value=product_data)
                    print(f"send {product_data}")

        await self.mongo.send_lamoda_data(self.kafka.consumer_lamoda)
