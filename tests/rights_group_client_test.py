from .fixtures import base_client, rights_group_client
from xflow_client import RightsGroupClient

def test_get_all_rights_groups(rights_group_client):
    groups = rights_group_client.get_all_rights_groups()
    assert isinstance(groups, list)

def test_get_rights_group(rights_group_client):
    group = rights_group_client.get_rights_group("BKF - Mobil i Odense")
    assert group is not None

def test_get_all_rights_groups_with_shared(rights_group_client):
    groups = rights_group_client.get_all_rights_groups(with_shared=True)
    assert isinstance(groups, list)

