from abc import ABC, abstractmethod
import aiohttp
from bs4 import BeautifulSoup


class AbstractParser(ABC):
    BASE_URL: NotImplemented = None
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }

    async def get_soup(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.HEADERS) as page:
                soup = BeautifulSoup(await page.text(), "lxml")
                return soup

    @abstractmethod
    async def parse(self):
        pass

