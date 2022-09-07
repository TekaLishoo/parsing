from kafka import KafkaConsumer, KafkaProducer
from json import dumps, loads
import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from parsing_scripts.base_parser import AbstractParser


class LamodaParser(AbstractParser):
    BASE_URL = "https://lamoda.by"

    async def parse(self):
        soup = await self.get_soup(self.BASE_URL)
        a_list = soup.find_all('a', attrs={'class': 'x-footer-seo-menu-tab-links__item'})
        visited_products = set()
        for a in a_list:
            actual_url = self.BASE_URL + a.attrs['href']
            actual_soup = await self.get_soup(actual_url)
            actual_a_list = actual_soup.find_all('a', attrs={'class': 'x-product-card__link'})
            for i in actual_a_list:
                print(f'{i.get_text()}')



