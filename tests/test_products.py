import pytest
from playwright.sync_api import sync_playwright
from services.product_api import ProductAPI

def test_get_all_products():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        product_api = ProductAPI(request_context)

        response = product_api.get_all_products()

        assert response.status == 200

        data = response.json()
        assert isinstance(data, list)

