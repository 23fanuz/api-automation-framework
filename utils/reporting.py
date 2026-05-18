import allure
import json


def attach_json(data, name: str):
    """
    Attaches formatted JSON data to Allure reports.

    This centralizes reporting behavior, keeping tests cleaner.
    """

    allure.attach(
        json.dumps(data, indent=4),
        name=name,
        attachment_type=allure.attachment_type.JSON
    )


def attach_request_response(method, endpoint, payload, response):
    """
    Automatically attaches API request/response details to Allure.
    """

    request_data = {
        "method": method,
        "endpoint": endpoint,
        "payload": payload
    }

    response_data = {
        "status": response.status,
        "body": response.json()
    }

    attach_json(request_data, "API Request")
    attach_json(response_data, "API Response")
