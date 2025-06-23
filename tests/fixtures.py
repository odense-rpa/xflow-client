import pytest
import os

from dotenv import load_dotenv
from xflow_client import XFlowClient, ProcessClient, ValueListClient

load_dotenv(dotenv_path="env.local")

@pytest.fixture(scope="session")
def base_client():
    instance = os.getenv("INSTANCE")
    api_key = os.getenv("API_KEY")
   
    if not all([instance, api_key]):
        raise ValueError("INSTANCE and API_KEY must be set in env.local")

    return XFlowClient(
        instance=instance,
        token=api_key
    )

@pytest.fixture
def process_client(base_client): # noqa
    return ProcessClient(base_client)

@pytest.fixture
def value_list_client(base_client): # noqa
    return ValueListClient(base_client)