from services.base_api_client import BaseAPIClient
from config.settings import Settings


class UserAPI(BaseAPIClient):
    """
    UserAPI takes care of all user-related api operations.

    This is a service layer abstraction that isolates endpoint login from
    test logic
    """

    # Initialize base client with shared API context and base URL
    def __init__(self, api_context):
        super().__init__(api_context, Settings.BASE_URL)

    def get_all_users(self):
        """
        GET /users
        :returns list of all users
        """
        return self.get("/users")

    def create_user(self, payload):
        """
        POST /users
        Creates a new user using the provided payload
        Note: FakeStoreAPI only returns ID, not a full user object.
        """
        return self.post("/users", data=payload)
