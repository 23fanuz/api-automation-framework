import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        context = p.request.new_context()
        yield context
        context.dispose()
