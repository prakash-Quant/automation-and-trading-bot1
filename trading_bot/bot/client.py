import logging
from binance.client import Client

class BinanceTestnetClient:
    def __init__(self, api_key, api_secret):
        if not api_key or not api_secret:
            raise ValueError("API Key and Secret Key cannot be empty!")

        logging.info("Initializing Binance Testnet Client...")
        self.client = Client(api_key, api_secret, testnet=True)

    def get_raw_client(self):
        return self.client
