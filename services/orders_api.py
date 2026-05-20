from services.base_api_client import BaseAPIClient
from config.settings import Settings


class CartsAPI(BaseAPIClient):

    """
    Service layer for Cart endpoints.
    Responsible for:
    - abstracting order/cart API operations

    """

    def __init__(self, api_context):
        super().__init__(api_context, Settings.BASE_URL)

    def get_all_carts(self):
        return self.get("/carts")

    def add_new_cart(self, payload):
        return self.post("/carts", payload)

