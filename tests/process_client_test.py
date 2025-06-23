from .fixtures import base_client, process_client
from xflow_client import ProcessClient

def test_start_process(process_client):
    data = {
        "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "processTemplateId": "f3508e75-87d0-467e-afce-5331c1dcdf64",
        "anotherUserId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "fillOutForAnotherUser": True,
        "startForAnotherUser": True
    }
    process = process_client.start_process(data)
    assert process is not None
    assert "id" in process    

def test_get_process(process_client):
    process = process_client.get_process("d4ad80b0-8bd1-453b-8e05-42df4bf5b6be")
    assert process is not None

def test_search_processes(process_client):
    query = {"status": "active"}
    processes = process_client.search_processes(query)
    assert isinstance(processes, list)
    assert len(processes) > 0

def test_advance_process(process_client):
    process = process_client.advance_process("d4ad80b0-8bd1-453b-8e05-42df4bf5b6be")
    assert process is not None
    assert "status" in process
    assert process["status"] == "advanced"

def test_reject_process(process_client):
    process = process_client.reject_process("d4ad80b0-8bd1-453b-8e05-42df4bf5b6be", 1, "Test rejection note")
    assert process is not None
    assert "status" in process
    assert process["status"] == "rejected"

def test_get_document(process_client):
    document = process_client.get_document("d4ad80b0-8bd1-453b-8e05-42df4bf5b6be")
    assert document is not None
    assert "id" in document
    assert document["id"] == "d4ad80b0-8bd1-453b-8e05-42df4bf5b6be" 
