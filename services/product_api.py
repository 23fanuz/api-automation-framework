from services.base_api_client import BaseAPIClient


class ProductAPI(BaseAPIClient):
    def __init__(self, api_context):
        super().__init__(api_context, "https://fakestoreapi.com")

    def get_all_products(self):
        return self.get("/products")
