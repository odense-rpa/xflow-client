from xflow_client import XFlowClient
from httpx import HTTPStatusError

class RightsGroupClient:
    def __init__(self, client: XFlowClient):
        """Initialize the RightsGroupClient with an XFlowClient instance.

        :param client: An instance of XFlowClient.
        """
        self.client = client

    def get_rights_group(self, name: str) -> dict | None:
        """Get a rights group by name.

        :param name: The name of the rights group.
        :return: The rights group data as a dict, or None if not found.
        """
        try:
            response = self.client.get(f"/RightsGroup/{name}")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise

    def get_all_rights_groups(self, with_shared: bool = False) -> list:
        """Get all rights groups for the organisation.

        :param with_shared: Whether to include shared rights groups.
        :return: A list of rights groups.
        """
        try:
            response = self.client.get(f"/RightsGroup/GetAll/{str(with_shared).lower()}")
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return []
            raise

    def create_rights_group(self, name: str, shared: bool = False) -> list:
        """Create a new rights group.

        :param name: The name of the rights group to create.
        :param shared: Whether the rights group should be shared.
        :return: The created rights group(s) as a list.
        """
        try:
            response = self.client.post(
                "/RightsGroup/Create",
                json={},
                params={"name": name, "shared": shared}
            )
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 400:
                return []
            raise

    def update_rights_group(self, name: str, new_name: str, shared: bool = False) -> list:
        """Update an existing rights group.

        :param name: The current name of the rights group.
        :param new_name: The new name for the rights group.
        :param shared: Whether the rights group should be shared.
        :return: The updated rights group(s) as a list.
        """
        try:
            response = self.client.put(
                "/RightsGroup/Update",
                json={},
                params={"name": name, "newName": new_name, "shared": shared}
            )
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 400:
                return []
            raise

    def delete_rights_group(self, name: str) -> dict | None:
        """Delete a rights group by name.

        :param name: The name of the rights group to delete.
        :return: The result as a dict, or None if not found.
        """
        try:
            response = self.client.delete(
                "/RightsGroup/Delete",
                params={"name": name}
            )
            return response.json()

        except HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise
