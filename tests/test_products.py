from services.product_api import ProductAPI
from models.product_model import Product
import allure


def test_get_all_products(api_context):
    product_api = ProductAPI(api_context)

    with allure.step("Send GET request to /products"):
        response = product_api.get_all_products()

    with allure.step("Verify status code is 200"):
        assert response.status == 200

    with allure.step("Parse response JSON"):
        products = response.json()

    with allure.step("Validate response schema using Pydantic"):
        validated_products = [Product(**product) for product in products]

    with allure.step("Verify at least one product exists"):
        assert len(validated_products) > 0

