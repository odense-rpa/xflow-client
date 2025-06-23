from .fixtures import base_client, value_list_client
from xflow_client import ValueListClient

def test_search_value_lists(value_list_client):     
    value_list = value_list_client.search_value_lists("RPA")
    assert len(value_list) > 0

def test_get_value_items_from_value_list(value_list_client):
    value_list = value_list_client.search_value_lists("RPA")
    assert len(value_list) > 0

    value_items = value_list_client.get_value_items_from_value_list(value_list[0]["id"])
    assert len(value_items) > 0
    assert "key" in value_items["valueListData"][0]
    assert "value" in value_items["valueListData"][0]