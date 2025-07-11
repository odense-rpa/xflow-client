from .fixtures import base_client, process_client
from xflow_client import ProcessClient


def test_start_process(process_client):
    data = {
        "userId": "03ac653e-edce-43c1-b2a2-4a69b09014a8",
        "processTemplateId": "f3508e75-87d0-467e-afce-5331c1dcdf64",
        "anotherUserId": "03ac653e-edce-43c1-b2a2-4a69b09014a8",
        "fillOutForAnotherUser": False,
        "startForAnotherUser": False,
    }
    process = process_client.start_process(data)
    assert process is not None
    assert "id" in process


def test_get_process(process_client):
    process = process_client.get_process("d8f629e8-1a4e-42b9-a34e-af740a2f33ba")
    assert process is not None


def test_search_processes(process_client):    
    query = {
        "text": "RPA",
        "processTemplateIds": [
            "401"
        ],
        "startIndex": 0,        
        "createdDateFrom": "01-01-1980",
        "createdDateTo": "01-07-2025",
    }
    processes = process_client.search_processes(query)
    assert len(processes) > 0


def test_search_processes_by_current_activity(process_client):
    activity_name = "RPAIntegration"

    query = {
        "text": "RPA",
        "processTemplateIds": [
            "401"
        ],
        "startIndex": 0,        
        "createdDateFrom": "01-01-1980",
        "createdDateTo": "01-07-2025",
    }

    processes = process_client.search_processes_by_current_activity(query, activity_name)
    assert len(processes) > 0

def test_update_process(process_client):
    query = {
        "text": "OPGAVEFLYTNING MELLEM MEDARBEJDERE I NEXUS",
        "processTemplateIds": [
            "714"
        ],
        "startIndex": 0,        
        "createdDateFrom": "01-01-1980",
        "createdDateTo": "01-07-2025",
    }

    processes = process_client.search_processes_by_current_activity(query, activity_name = "RPAIntegration")
    process_id = processes[0].get("publicId")    
    
    assert process_id is not None
    
    data = {
        "formValues": [
            {
                "elementIdentifier": "FraMedarbejder",
                "valueIdentifier": "Tekst",
                "value": "Mojn"      
            },
            {
                "elementIdentifier": "TilMedarbejder",
                "valueIdentifier": "Tekst",
                "value": "Hej"      
            }
        ]        
    }

    response = process_client.update_process(process_id, data)
    assert response is not None
    assert response.status_code == 200

def test_advance_process(process_client):
    response = process_client.advance_process("6c35c34f-c1dd-41a7-a502-ab8eed233bed")
    assert response is not None
    assert response.status_code == 200


def test_reject_process(process_client):
    response = process_client.reject_process(
        "63f033a1-9748-44c6-ba40-4459bd269389", 887642, "Test rejection note"
    )
    assert response is not None
    assert response.status_code == 200


def test_get_document(process_client):
    document = process_client.get_document("53837f40-e561-4103-88d7-e8a2d7cb17ec")
    assert document is not None
    assert "id" in document
    assert document["id"] == "d4ad80b0-8bd1-453b-8e05-42df4bf5b6be"

def test_find_process_element_value(process_client):
    query = {
        "text": "OPGAVEFLYTNING MELLEM MEDARBEJDERE I NEXUS",
        "processTemplateIds": [
            "714"
        ],
        "startIndex": 0,        
        "createdDateFrom": "01-01-1980",
        "createdDateTo": "01-07-2025",
    }

    processes = process_client.search_processes_by_current_activity(query, activity_name = "RPAIntegration")
    process_id = processes[0].get("publicId")    
    
    assert process_id is not None
    
    value = process_client.find_process_element_value(processes[0], "FraMedarbejder", "Tekst")
    assert value is not None
    