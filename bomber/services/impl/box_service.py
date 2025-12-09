import ssl
import certifi
import aiohttp
from bomber.services.bomber_service import BomberService


class BoxService(BomberService):
    async def send_request(self, phone_number: str):
        url = f"https://app.snapp-box.com/api/getouei/api/customer/v2/auth/{phone_number.lstrip('+')}/info"

        headers = {
            'accept': '*/*',
            'accept-language': 'fa-IR',
            'appversion': '5.15.2',
            'clienttype': 'pwa',
            'content-type': 'application/json',
            'locale': 'fa-IR',
            'platform': 'web',
            'priority': 'u=1, i',
            'referer': 'https://app.snapp-box.com/login',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'cookie': '_ym_uid=1736155536713400504; _ga_28TD5C44LR=GS1.1.1737744886.13.1.1737745699.56.0.0; _gcl_au=1.1.171830603.1759752793; _ym_d=1759752794; _ga=GA1.1.514329727.1736155534; _ym_debug=0; _clck=3rn6cl^2^g1p^0^1832; _ym_isad=2; _clsk=1sz78ay^1765276948646^3^1^l.clarity.ms/collect; _ga_LMCP2XVPV6=GS2.1.s1765276941$o98$g1$t1765276962$j39$l0$h1977730068'
        }

        ssl_context = ssl.create_default_context(cafile=certifi.where())
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
            async with session.get(url, headers=headers) as resp:
                return resp
