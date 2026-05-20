from services.product_api import ProductAPI
import allure
from utils.validation import  validate_response


def test_get_all_products(api_context):
    product_api = ProductAPI(api_context)

    with allure.step("Send GET request to /products"):
        response = product_api.get_all_products()

    with allure.step("Verify status code is 200"):
        assert response.status == 200

    with allure.step("Validate response schema using Pydantic"):
        products = validate_response("GET", "/products", response)

    with allure.step("Verify at least one product exists"):
        assert len(products) > 0
