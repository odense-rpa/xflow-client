from xflow_client import XFlowClient
from httpx import HTTPStatusError

class UserClient:
    def __init__(self, client: XFlowClient):
        """Initialize the UserClient with an XFlowClient instance.
        
        :param client: An instance of XFlowClient.
        """
        self.client = client

    def get_user(self, user_id: str):
        """Get a specific user by their ID.
        
        :param user_id: The ID of the user to retrieve.
        :return: The user data as a JSON object or None if not found.
        """
        try:
            response = self.client.get(f"/User/{user_id}")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise

    def search_users(self, email: str = None, cpr: str = None):
        if not email and not cpr:
            raise ValueError("At least one of email or CPR must be provided.")

        try:
            response = self.client.get("/User/Search", params={
                "email": email,
                "cpr": cpr
            })

            if response.status_code == 204:
                return []
            
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return []
            raise