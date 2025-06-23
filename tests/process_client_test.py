from .fixtures import base_client, process_client
from xflow_client import ProcessClient

def test_get_process_templates(process_client):     
    process_templates = process_client.get_process_templates()
    assert len(process_templates) > 0