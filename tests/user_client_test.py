from .fixtures import base_client, user_client
from xflow_client import UserClient

def test_get_user(user_client):
    user = user_client.get_user("03ac653e-edce-43c1-b2a2-4a69b09014a8")
    assert user is not None
    assert user["email"] == "simof@odense.dk"

def test_search_users(user_client):
    users = user_client.search_users(email = "simof@odense.dk", cpr = None)
    assert len(users) > 0
    