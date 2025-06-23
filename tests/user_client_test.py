from .fixtures import base_client, user_client
from xflow_client import UserClient

def test_get_user(user_client):
    user = user_client.get_user("")
    assert isinstance(user, UserClient)
    assert user.id == base_client.user_id

def test_search_users(user_client):
    users = user_client.search_users(email = "simof@odense.dk", cpr = None)
    assert isinstance(users, list)
    assert all(isinstance(user, UserClient) for user in users)