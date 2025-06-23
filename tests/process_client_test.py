from .fixtures import base_client, process_template_client
from xflow_client import ProcessTemplateClient

def test_get_process_templates(process_template_client):     
    process_templates = process_template_client.get_process_templates()
    assert len(process_templates) > 0

def test_get_process_template(process_template_client):
    process_template = process_template_client.get_process_template("d4ad80b0-8bd1-453b-8e05-42df4bf5b6be")
    assert process_template is not None    

def test_get_process_template_documentation(process_template_client):
    documentation = process_template_client.get_process_template_documentation("d4ad80b0-8bd1-453b-8e05-42df4bf5b6be")
    assert documentation is not None        