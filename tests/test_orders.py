import allure

from services.orders_api import CartsAPI
from utils.validation import validate_response


def test_get_all_carts(api_context):
    """
   Validate retrieval of all carts
    """

    cart_api = CartsAPI(api_context)

    with allure.step("Send GET request to /carts"):
        response = cart_api.get_all_carts()

    with allure.step("Verify status code is 200"):
        assert response.status == 200

    with allure.step("Validate order schema"):
        orders = validate_response("GET", "/carts", response)

    with allure.step("Verify at least one order exists"):
        assert len(orders) > 0
