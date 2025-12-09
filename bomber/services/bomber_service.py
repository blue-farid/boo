from abc import ABC, abstractmethod

class BomberService(ABC):
    """all new services should implement this interface (strategy pattern)"""
    @abstractmethod
    async def send_request(self, phone_number: str):
        """call the service with the phone number"""
        pass