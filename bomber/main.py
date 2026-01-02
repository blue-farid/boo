import asyncio

from bomber.services.impl.snapp_service import SnappService
from bomber.services.impl.box_service import BoxService
from bomber.services.impl.snapp_food import SnappFoodService
from bomber.services.impl.wallex_service import WallexService
from bomber.services.impl.tetherland_service import TetherlandService


SERVICES = [SnappService(), BoxService(), SnappFoodService(), WallexService(), TetherlandService()]


async def run_bomber(phone_number: str):
    tasks = [service.send_request(phone_number) for service in SERVICES]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for service, result in zip(SERVICES, results):
        print(f"{service.__class__.__name__}: {result}")


if __name__ == "__main__":
    phone = input("Enter phone number: ")
    asyncio.run(run_bomber(phone))
