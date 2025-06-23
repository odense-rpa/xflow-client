import os
import logging
from dotenv import load_dotenv

from src.xflow_client.client import XFlowClient
# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Retrieve instance and token from environment variables
instance = os.getenv("INSTANCE")
token = os.getenv("TOKEN")

client = XFlowClient(
    instance=instance,
    token=token
)
print(client)


