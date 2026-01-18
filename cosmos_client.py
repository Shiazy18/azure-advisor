# cosmos_client.py
import os
from azure.cosmos import CosmosClient
from datetime import datetime
import uuid
from azure.identity import DefaultAzureCredential

# Load env variables
COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
COSMOS_DATABASE = os.getenv("COSMOS_DATABASE")
COSMOS_QUERIES_CONTAINER = os.getenv("COSMOS_QUERIES_CONTAINER")

credential = DefaultAzureCredential()

# client = CosmosClient(
#     url=COSMOS_ENDPOINT,
#     credential=credential
# )
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.get_database_client(COSMOS_DATABASE)
container = database.get_container_client(COSMOS_QUERIES_CONTAINER)

def store_gpt_output(payload, gpt_output):
    """
    Stores the GPT architecture options along with input payload in Cosmos DB.
    Each record will have:
    - id: unique identifier
    - timestamp
    - payload: the original user input
    - suggestions: GPT output
    """
    doc = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "payload": payload,
        "suggestions": gpt_output
    }
    container.create_item(body=doc)
    return doc["id"]
