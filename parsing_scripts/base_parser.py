from abc import ABC, abstractmethod
import aiohttp
from bs4 import BeautifulSoup
import requests
from di.controller_general import ControllerGeneral
from config.config import Settings


class AbstractParser(ABC):
    """
    An abstact model for parsers.
    """

    BASE_URL: NotImplemented = None
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }
    general_settings = ControllerGeneral(Settings())

    async def get_soup(self, url):
        """
        Returns a soup object for given url.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.HEADERS) as page:
                soup = BeautifulSoup(await page.text(), "lxml")
                return soup

    def auth(self, auth_url, base_url):
        """
        Returns a data from base_url, which requires token authentication
        """
        resp = requests.post(
            f"{auth_url}"
            f"?client_id={self.general_settings.client_id}"
            f"&client_secret={self.general_settings.secret_key}"
            f"&grant_type=client_credentials"
        )
        data = requests.get(
            base_url,
            headers={
                "Authorization": f'Bearer {resp.json()["access_token"]}',
                "Client-Id": self.general_settings.client_id,
            },
        )
        return data

    @abstractmethod
    async def parse(self):
        pass
