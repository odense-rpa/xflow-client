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

    def update_value_list(self, value_list_id: str, value_list_data: dict):
        """Update a value list with new data.
        :param value_list_id: The ID of the value list to update.
        :param value_list_data: A dictionary containing the updated value list data. The dict needs three keys:
            - 'key': The key of the value item.
            - 'value': The value of the value item.
            - 'oprettetAf': The user or system that created the value item. Typically 'System'"""
        try:
            response = self.client.put(
                f"/ValueList/{value_list_id}/Values",
                json={"ValueListData": value_list_data})
            # Hvis svar ikke indeholder JSON, returner fx status code eller True
            if response.status_code == 204 or not response.content:
                return None  # eller True / response.status_code
            return response.json()
        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise