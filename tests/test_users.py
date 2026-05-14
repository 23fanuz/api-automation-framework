import allure

from services.user_api import UserAPI
from models.user_model import User
from models.user_model import UserResponse
from utils.data_generator import generate_user_payload
from utils.validation import validate_response


def test_get_all_users(api_context):
    user_api = UserAPI(api_context)

    with allure.step("Send GET request to /users"):
        response = user_api.get_all_users()

    with allure.step("Attach raw response"):
        allure.attach(
            str(response.json()),
            name="Users response JSON",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Verify status code is 200"):
        assert response.status == 200

    with allure.step("Parse JSON response"):
        users = response.json()

    with allure.step("Validate user schema using Pydantic"):
        validated_users = [User(**user) for user in users]

    with allure.step("Verify at least one user exists"):
        assert len(validated_users) > 0


def test_create_user(api_context):
    """
    Validates user creation endpoint.

    This test:
    - Generates dynamic user data
    - Sends POST request
    - Validates API response
    """
    user_api = UserAPI(api_context)

    with allure.step("Generate dynamic user payload"):
        # Create fake user using Faker
        payload = generate_user_payload()

    with allure.step("Send POST request to create user"):
        response = user_api.create_user(payload)

    with allure.step("Attach request payload"):
        allure.attach(
            str(payload),
            name="Request Payload",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Verify status code is 201"):
        assert response.status == 201

    with allure.step("Validate response contains ID only"):
        # FakeStoreAPI only returns ID
        created_user = validate_response(UserResponse, response)
        assert created_user.id is not None
