from utils.logger import get_logger
from utils.reporting import attach_request_response


class BaseAPIClient:
    def __init__(self, api_context, base_url: str):
        self.api_context = api_context
        self.base_url = base_url
        self.logger = get_logger(self.__class__.__name__)

    def get(self, endpoint: str):
        response = self.api_context.get(f"{self.base_url}{endpoint}")

        attach_request_response(
            method="GET",
            endpoint=endpoint,
            payload=None,
            response=response
        )

        return response

    def post(self, endpoint: str, data=None):
        response = self.api_context.post(
            f"{self.base_url}{endpoint}",
            data=data
        )

        attach_request_response(
            method="POST",
            endpoint=endpoint,
            payload=data,
            response=response
        )

        return response

    def delete(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"DELETE {url}")

        response = self.api_context.delete(url)

        self.logger.info(f"Response status: {response.status}")
        return response
