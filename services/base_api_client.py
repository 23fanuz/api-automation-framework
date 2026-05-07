from utils.logger import get_logger
class BaseAPIClient:
    def __init__(self, api_context, base_url: str):
        self.api_context = api_context
        self.base_url = base_url
        self.logger = get_logger(self.__class__.__name__)

    def get(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET{url}")

        response = self.api_context.get(url)
        self.logger.info(f"Response status: {response.status}")
        return response


    def post(self, endpoint: str, data=None):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST {url}")

        response = self.api_context.post(url, data=data)

        self.logger.info(f"Response status: {response.status}")
        return response

    def delete(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"DELETE {url}")

        response = self.api_context.delete(url)

        self.logger.info(f"Response status: {response.status}")
        return response
