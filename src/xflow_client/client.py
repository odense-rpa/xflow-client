import httpx
import logging
import json
from authlib.integrations.httpx_client import OAuth2Client
from urllib.parse import urljoin

def _format_json(data: dict) -> str:
    """Format JSON data for logging.
    :param data: The JSON data to format.
    :return: A formatted string representation of the JSON data.
    """
    return json.dumps(data, indent=2)
instance = "odense-test"
token = "abc"

class XFlowClient:
    api: dict

    def __init__(self, instance: str, token: str):
        """Initialize the XFlowClient with the instance URL and token.
        :param instance: The base URL of the XFlow instance.
        :param token: The authentication token for the XFlow instance.
        """

        if not instance:
            raise ValueError("Instance URL must be provided.")
        
        self.token = {
            "headers": {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }       
        }
        self.base_url = f"https://api.{instance}.xflow.dk/"

        # Set up logging
        self.logger = logging.getLogger(__name__)

        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("httpcore").setLevel(logging.WARNING)

        # Set up OAuth2 client
        self.client = OAuth2Client(
            token=self.token,
            base_url=self.base_url
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


    def _handle_errors(self, response: httpx.Response):
        if response.is_error:
            self.logger.error(f"Error {response.status_code}: {response.text}")
        response.raise_for_status() 