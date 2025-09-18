from xflow_client import XFlowClient
from httpx import HTTPStatusError

class DocumentClient:
    def __init__(self, client: XFlowClient):
        """Initialize the DocumentClient with an XFlowClient instance.
        
        :param client: An instance of XFlowClient.
        """
        self.client = client

    def hent_dokument_med_metadata(self, dokument_id: str) -> dict|None:
        """
        Henter et dokument med tilhørende metadata basert på dokument_id.

        Args:
            dokument_id (str): ID-en til dokumentet som skal hentes.

        Returns:
            dict: En ordbok som inneholder dokumentdata og metadata.
        """

        try:
            response = self.client.get(f"/DocumentWithMetadata/{dokument_id}")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise            
        