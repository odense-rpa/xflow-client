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
            connect=20.0,  # Time to connect to the server
            read=60.0,     # Time to read the response
            write=30.0,    # Time to send the request
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
        
    def is_non_empty(self, val):
        if val is None:
            return False
        if isinstance(val, (dict, list)) and not val:
            return False
        if isinstance(val, str) and not val.strip():
            return False
        return True

    def extract_referable_elements_with_values(self, element):
        children = []
        for child in element.get("children", []):
            child_result = self.extract_referable_elements_with_values(child)
            if child_result is not None:
                children.append(child_result)
        if self.is_non_empty(element.get("values")):
            result = {
                "identifier": element.get("identifier"),
                "values": element.get("values")
            }
            if children:
                result["children"] = children
            return result
        if children:
            if len(children) == 1:
                return children[0]
            return children
        return None

    def traverse_json_for_referable_elements(self, obj):
        results = []
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "elementer" and isinstance(value, list):
                    for element in value:
                        res = self.extract_referable_elements_with_values(element)
                        if res is not None:
                            if isinstance(res, list):
                                results.extend(res)
                            else:
                                results.append(res)
                else:
                    results.extend(self.traverse_json_for_referable_elements(value))
        elif isinstance(obj, list):
            for item in obj:
                results.extend(self.traverse_json_for_referable_elements(item))
        return results