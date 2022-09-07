from parsing_scripts.base_parser import AbstractParser


class TwitchParser(AbstractParser):
    BASE_URL = "https://api.twitch.tv/helix/streams"

    async def parse(self):
        soup = await self.get_soup(self.BASE_URL)
