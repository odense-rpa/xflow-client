from xflow_client import XFlowClient
from httpx import HTTPStatusError

class ValueListClient:
    def __init__(self, client: XFlowClient):
        """Initialize the ValueListClient with an XFlowClient instance.
        
        :param client: An instance of XFlowClient.
        """
        self.client = client
        

    def search_value_lists(self, search_term: str):
        """Search for value lists by a search term.
        
        :param search_term: The term to search for in value lists.
        :return: A list of value lists matching the search term.
        """
        try:
            response = self.client.get(f"/ValueList/Search?name={search_term}")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise
