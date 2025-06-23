from xflow_client import XFlowClient
from httpx import HTTPStatusError

class ProcessClient:
    def __init__(self, client: XFlowClient):
        """Initialize the ProcessClient with an XFlowClient instance.
        
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