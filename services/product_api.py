from playwright.sync_api import APIRequestContext


class ProductAPI:
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context
        self.base_url = "https://fakestoreapi.com"

    def get_all_products(self):
        response = self.request.get(f"{self.base_url}/products")
        return response
