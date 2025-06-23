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

    def get_value_items_from_value_list(self, value_list_id: str):
        """Get value items from a specific value list.
        
        :param value_list_id: The ID of the value list to retrieve items from. Can be found in the response of search_value_lists.
        :return: A list of value items in the specified value list.
        """
        try:
            response = self.client.get(f"/ValueList/{value_list_id}/Values")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise