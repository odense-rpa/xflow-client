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

def test_update_value_list(value_list_client):
    response = value_list_client.get_value_items_from_value_list("37493516-8612-44e9-9767-9250351eb658")
    value_list_data = response["valueListData"]

    assert isinstance(value_list_data, list)
    assert len(value_list_data) > 0
    
    new_item = {
        "key": "5",
        "value": "test_værdi",
        "vaerdilisteId": 129,
        "oprettetAf": "System"
    }

    updated_value_list_data = value_list_data + [new_item]

    updated_payload = {"valueListData": updated_value_list_data}
    value_list_client.update_value_list("37493516-8612-44e9-9767-9250351eb658", updated_payload)

    refreshed = value_list_client.get_value_items_from_value_list("37493516-8612-44e9-9767-9250351eb658")
    refreshed_items = refreshed["valueListData"]
    match = next((item for item in refreshed_items if item["value"] == "test_værdi"), None)
    assert match is not None

    # Oprydning: fjern testitem igen
    cleaned_list = [item for item in refreshed_items if item["key"] != "5"]
    cleanup_payload = {"valueListData": cleaned_list}
    value_list_client.update_value_list("37493516-8612-44e9-9767-9250351eb658", cleanup_payload)
    
