from .fixtures import base_client, value_list_client
from xflow_client import ValueListClient

def test_get_process_templates(value_list_client):     
    value_list = value_list_client.search_value_lists("RPA")
    assert len(value_list) > 0