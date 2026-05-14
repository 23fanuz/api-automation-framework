import allure

from services.user_api import UserAPI
from models.user_model import User


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

