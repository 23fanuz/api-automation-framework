from utils.schema_registry import SCHEMA_REGISTRY


def  validate_response(method: str, endpoint: str, response):
    """
    Automatically validates API responses based on endpoint mappings + HTTP method

    Creates a centralized contract validation system.
    """

    try:
        response_json = response.json()

        # Find expected schema
        model = SCHEMA_REGISTRY.get((method, endpoint))

        if not model:
            raise ValueError(f"No schema registered for {method} {endpoint}")

        if isinstance(response_json, list):
            return [model(**item) for item in response_json]

        return model(**response_json)

    except Exception as e:
        raise AssertionError(
            f"Validation failed for endpoint {endpoint}: {str(e)}\n"
            f"Response JSON: {response_json}"
        )
