from services.product_api import ProductAPI


def test_get_all_products(api_context):
    product_api = ProductAPI(api_context)

    response = product_api.get_all_products()

    assert response.status == 200
    assert isinstance(response.json(), list)
