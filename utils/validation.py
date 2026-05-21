from pydantic import ValidationError


class APIContractViolationError(AssertionError):
    """
    Custom exception for clean API contract violation reporting.
    """
    pass


def validate_payload(response, model):
    """
        Validates a raw response against a provided Pydantic model
        """

    try:
        response_json = response.json()
    except ValueError:
        raise APIContractViolationError("Failed to parse response as JSON")

    try:
        if isinstance(response_json, list):
            return [model(**item) for item in response_json]
        return model(**response_json)

    except ValidationError as e:
        # Catch Pydantic's specific error and format it
        error_msg = f"Contract Violation for {model.__name__}:\n"
        for error in e.errors():
            # e.errors() -> a list of dictionaries with field locations and messagesa
            field = " -> ".join([str(loc) for loc in error['loc']])
            error_msg += f"- Field '{field}: {error['msg']}\n"

        raise APIContractViolationError(error_msg)
