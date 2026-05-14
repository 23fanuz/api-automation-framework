from pydantic import BaseModel
from typing import Type


def validate_response(model: Type[BaseModel], response):
    """
    Central validation layer for all API tests.

    This function:
    - parses JSON response
    - validates against a Pydantic model
    - returns an object

    """
    try:
        response_json = response.json()

        # Validate and return typed obj
        validated_object = model(**response_json)

        return validated_object

    except Exception as e:
        raise AssertionError(
            f"Response validation failed for {model.__name__}: {str(e)}\n"
            f"Response JSON: {response_json}"
        )

