from .fixtures import base_client, document_client

def test_hent_dokument_med_metadata(document_client):
    document_id = "1ed6f702-4ddd-4b82-ab14-e8eec3a871ed" 
    dokument = document_client.hent_dokument_med_metadata(document_id)
    assert dokument is not None