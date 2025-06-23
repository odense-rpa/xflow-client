from xflow_client import XFlowClient
from httpx import HTTPStatusError

class ProcessTemplateClient:
    def __init__(self, client: XFlowClient):
        """Initialize the ProcessTemplateClient with an XFlowClient instance.
        
        :param client: An instance of XFlowClient.
        """
        self.client = client
        
    def get_process_templates(self):
        try:
            response = self.client.get("/ProcessTemplate/All")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise

    def get_process_template(self, template_id: str):
        try:
            response = self.client.get(f"/ProcessTemplate/{template_id}")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise

    def get_process_template_documentation(self, template_id: str):
        try:
            response = self.client.get(f"/ProcessTemplate/{template_id}/Documentation")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise