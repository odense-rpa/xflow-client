import httpx
import logging
import json

from urllib.parse import urljoin

def _format_json(data: dict) -> str:
    """Format JSON data for logging.
    :param data: The JSON data to format.
    :return: A formatted string representation of the JSON data.
    """
    return json.dumps(data, indent=2)

class XFlowClient:
    api: dict

    def __init__(self, instance: str, token: str):
        """Initialize the XFlowClient with the instance URL and token.
        :param instance: The base URL of the XFlow instance.
        :param token: The authentication token for the XFlow instance.
        """

        if not instance:
            raise ValueError("Instance URL must be provided.")
        
        self.headers = {
            "publicApiToken": f"{token}"            
        }
        self.base_url = f"https://api.{instance}.xflow.dk/"

        self.logger = logging.getLogger(__name__)
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("httpcore").setLevel(logging.WARNING)
        
        timeout = httpx.Timeout(
            connect=10.0,  # Time to connect to the server
            read=20.0,     # Time to read the response
            write=10.0,    # Time to send the request
            pool=5.0       # Time to wait for an available connection from the pool
        )

        self.client = httpx.Client(
            base_url=self.base_url, 
            headers=self.headers,
            timeout=timeout,
        )

    def _normalize_url(self, endpoint: str) -> str:
        """Ensure the URL is aboslute, handling relative URLS."""
        if endpoint.startswith("http://") or endpoint.startswith("https://"):
            return endpoint
        return urljoin(self.base_url, endpoint)
    
    def get(self, endpoint: str, **kwags) -> httpx.Response:
        url = self._normalize_url(endpoint)
        response = self.client.get(url, **kwags)
        self._handle_errors(response) # findes ikke atm
        return response
    
    def post(self, endpoint: str, json: dict, **kwargs) -> httpx.Response:
        url = self._normalize_url(endpoint)
        response = self.client.post(url, json=json, **kwargs)
        self._handle_errors(response)

        return response

    def put(self, endpoint: str, json: dict, **kwargs) -> httpx.Response:
        url = self._normalize_url(endpoint)

        response = self.client.put(url, json=json, **kwargs)
        self._handle_errors(response)
        return response

    def delete(self, endpoint: str, **kwargs) -> httpx.Response:
        url = self._normalize_url(endpoint)
        
        response = self.client.delete(url, **kwargs)
        self._handle_errors(response)
        return response

    def _handle_errors(self, response: httpx.Response):
        if response.is_error:
            self.logger.error(f"Error {response.status_code}: {response.text}")
        response.raise_for_status()
        