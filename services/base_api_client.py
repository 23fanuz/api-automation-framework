class BaseAPIClient:
    def __init__(self, api_context, base_url: str):
        self.api_context = api_context
        self.base_url = base_url

    def get(self, endpoint: str):
        return self.api_context.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint: str, data=None):
        return self.api_context.post(f"{self.base_url}{endpoint}", data=data)

    def delete(self, endpoint: str):
        return self.api_context.delete(f"{self.base_url}{endpoint}")