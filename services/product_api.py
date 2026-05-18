from services.base_api_client import BaseAPIClient
from config.settings import Settings


class ProductAPI(BaseAPIClient):
    def __init__(self, api_context):
        super().__init__(api_context, Settings.BASE_URL)

    def get_all_products(self):
        return self.get("/products")
