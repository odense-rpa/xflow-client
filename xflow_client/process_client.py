from xflow_client import XFlowClient
from httpx import HTTPStatusError

class ProcessClient:
    def __init__(self, client: XFlowClient):
        """Initialize the ProcessClient with an XFlowClient instance.
        
        :param client: An instance of XFlowClient.
        """
        self.client = client
        