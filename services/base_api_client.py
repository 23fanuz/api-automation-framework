from utils.logger import get_logger
from utils.reporting import attach_request_response
from utils.validation import validate_payload


class BaseAPIClient:
    def __init__(self, api_context, base_url: str):
        self.api_context = api_context
        self.base_url = base_url
        self.logger = get_logger(self.__class__.__name__)

    def get(self, endpoint: str, response_model=None, expected_status: int = 200):
        """Executes GET request and optionally validates response"""
        response = self.api_context.get(f"{self.base_url}{endpoint}")

        attach_request_response(
            method="GET",
            endpoint=endpoint,
            payload=None,
            response=response
        )

        if response.status != expected_status:
            raise AssertionError(
                f"HTTP Status Violation on GET {endpoint}:\n"
                f"Expected: {expected_status} | Actual: {response.status}\n"
                f"Response Body: {response.text()}"
            )

        if response_model:
            return validate_payload(response, response_model)

        return response

    def post(self, endpoint: str, data=None, response_model=None):
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
        if response_model:
            return validate_payload(response, response_model)

        return response

    def delete(self, endpoint: str, response_model=None):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"DELETE {url}")

        response = self.api_context.delete(url)

        if response_model:
            return validate_payload(response, response_model)

        return response
