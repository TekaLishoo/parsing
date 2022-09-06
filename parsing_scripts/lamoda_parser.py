from kafka import KafkaConsumer, KafkaProducer
from json import dumps, loads
import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup


HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }


async def get_soup(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as page:
            soup = BeautifulSoup(await page.text(), "lxml")
            return soup


async def lamoda_parser():
    url = 'https://www.lamoda.by'
    soup = await get_soup(url)
    a_list = soup.find_all('a', attrs={'class': 'x-footer-seo-menu-tab-links__item'})
    visited_products = set()
    for a in a_list:
        actual_url = url + a.attrs['href']
        actual_soup = await get_soup(actual_url)
        actual_a_list = actual_soup.find_all('a', attrs={'class': 'x-product-card__link'})
        for i in actual_a_list:
            print(f'{i.get_text()}')


    # producer = KafkaProducer(retries=5, bootstrap_servers=['kafka:9092'],
    #                          value_serializer=lambda x: dumps(x).encode('utf-8'))
    # d = producer.send('topic_test', value={'counter': '5'})
    # data = d.get()
    # print(f'send {data.topic}')
    #
    # consumer = KafkaConsumer(
    #     'topic_test',
    #     bootstrap_servers=['kafka:9092'],
    #     auto_offset_reset='earliest',
    #     enable_auto_commit=True,
    #     group_id='my-group-id',
    #     value_deserializer=lambda x: loads(x.decode('utf-8'))
    # )
    # for event in consumer:
    #     event_data = event.value
    #     # Do whatever you want
    #     print(f'received {event_data}')
