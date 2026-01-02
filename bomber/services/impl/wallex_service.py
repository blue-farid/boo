import ssl
import certifi
import aiohttp
from bomber.services.bomber_service import BomberService

active = False

class WallexService(BomberService):
    async def send_request(self, request_id: str):
        if (not active):
            return None
        url = "https://api.wallex.ir/v3/auth/forgot-password"

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "origin": "https://wallex.ir/",
            "platform": "web",
            "user-agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/143.0.0.0 Safari/537.36"
            ),
        }

        payload = {
            "request_id": request_id
        }

        ssl_context = ssl.create_default_context(cafile=certifi.where())

        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=ssl_context),
            timeout=aiohttp.ClientTimeout(total=10)
        ) as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                return resp.status, await resp.text()
