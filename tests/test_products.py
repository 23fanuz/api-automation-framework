from services.product_api import ProductAPI
from models.product_model import Product


def test_get_all_products(api_context):
    product_api = ProductAPI(api_context)

    response = product_api.get_all_products()

    assert response.status == 200

    products = response.json()
    validated_products = [Product(**product) for product in products]
    assert len(validated_products) > 0
