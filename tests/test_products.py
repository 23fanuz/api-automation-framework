import pytest
from playwright.sync_api import  sync_playwright

def test_get_all_products():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        response = request_context.get("https://fakestoreapi.com/products")
        assert response.status == 200

        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

