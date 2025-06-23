from xflow_client import XFlowClient
from httpx import HTTPStatusError

class ProcessClient:
    def __init__(self, client: XFlowClient):
        """Initialize the ProcessClient with an XFlowClient instance.
        
        :param client: An instance of XFlowClient.
        """
        self.client = client

    def start_process(self, data: dict):
        """Start a new process of a given type with the provided data.

        :param process_type: The type of the process to start.
        :param data: The data to initialize the process with.
        :return: The created process data as a JSON object.
        """
        try:
            response = self.client.post("/Process", json=data)
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise
    
    def get_process(self, process_id: str):
        """Get a specific process by its ID.
        
        :param process_id: The ID of the process to retrieve.
        :return: The process data as a JSON object or None if not found.
        """
        try:
            response = self.client.get(f"/Process/{process_id}")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise

    def search_processes(self, query: dict):
        """Search for processes based on a query string.
        
        :param query: The search query object (dict).
        :return: A list of processes matching the query.
        """
        try:
            response = self.client.post("/Process/Search", json=query)
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return []
            raise

    def search_processes_by_current_activity(self, activity_id: int):
        """Search for processes by the current activity ID.
        
        :param activity_id: The ID of the current activity to search for.
        :return: A list of processes that are currently at the specified activity.
        """
        try:
            pass
            # TODO: Implement the actual endpoint for searching by current activity

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return []
            raise    

    def advance_process(self, process_id: str):
        """Advance a process to the next step.
        
        :param process_id: The ID of the process to advance.        
        :return: The updated process data as a JSON object or None if not found.
        """
        try:
            response = self.client.post(f"/Process/{process_id}/Advance", json={})
            return response

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise

    def reject_process(self, process_id: str, activity_id: int, note = None):
        """Reject a process.
        
        :param process_id: The ID of the process to reject.
        :return: The updated process data as a JSON object or None if not found.
        """
        try:
            response = self.client.post(f"/Process/{process_id}/Reject", json={"rejectedToActivityId": activity_id, "note": note})
            return response

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise

    def get_document(self, document_id: str):
        # Structured under ProcessClient to avoid a client for a single method.
        """Get a specific document by its ID.
        
        :param document_id: The ID of the document to retrieve.
        :return: The document data as a JSON object or None if not found.
        """
        try:
            response = self.client.get(f"/Document/{document_id}")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise