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

        # Set up logging
        self.logger = logging.getLogger(__name__)

        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("httpcore").setLevel(logging.WARNING)

        # Set up OAuth2 client
        self.client = httpx.Client(
            base_url=self.base_url, 
            headers=self.headers
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

        # Check if the endpoint is in the non-logging list
        if len([endpoint for endpoint in self._non_logging_endpoints if url.endswith(endpoint)]) == 0:
            self.logger.info(f"POST: {url} data: {_format_json(json)}")

        response = self.client.post(url, json=json, **kwargs)
        self._handle_errors(response)
        return response

    def put(self, endpoint: str, json: dict, **kwargs) -> httpx.Response:
        url = self._normalize_url(endpoint)

        if len([endpoint for endpoint in self._non_logging_endpoints if url.endswith(endpoint)]) == 0:
            self.logger.info(f"PUT: {url} data: {_format_json(json)}")

        response = self.client.put(url, json=json, **kwargs)
        self._handle_errors(response)
        return response

    def delete(self, endpoint: str, **kwargs) -> httpx.Response:
        url = self._normalize_url(endpoint)
        
        if len([endpoint for endpoint in self._non_logging_endpoints if url.endswith(endpoint)]) == 0:
            self.logger.info(f"DELETE: {url}")
        
        response = self.client.delete(url, **kwargs)
        self._handle_errors(response)
        return response

    def _handle_errors(self, response: httpx.Response):
        if response.is_error:
            self.logger.error(f"Error {response.status_code}: {response.text}")
        response.raise_for_status()
        