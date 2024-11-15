import os
import requests
from utils.db import client

db_name = os.getenv('DATABASE_NAME')
collection_name = os.getenv('COLLECTION_NAME')
openai_key = os.getenv("OPENAI_KEY")
vector_index_name = os.getenv('VECTOR_INDEX_NAME')

database = client[f"{db_name}"]
collection = database[f"{collection_name}"]

def getEmbedding(word: str):
    try:
        data = { "input": word, "model": "text-embedding-ada-002" }
        header = { "Authorization": f"Bearer {openai_key}", "Content-Type": "application/json" }
        response = requests.post("https://api.openai.com/v1/embeddings", json=data, headers=header)
        return response.content
    except Exception as e:
        raise e

async def search(word: str, limit: int = 30, filter: str = ""):
    queryVector = await getEmbedding(word)
    pipeline = [
        {
          "$vectorSearch": {
            "queryVector": queryVector,
            "filter": {
                "$gate": {
                    { "직군": { "$in": filter }}
                }
            },
            "path": "vectorEmbedding",
            "numCandidates": 100,
            "exact": False,
            "limit": limit,
            "index": f"{vector_index_name}",
          },
        },
        {
          "$project": {
            "_id": 0,
            "recruitmentId": 1,
            "score": { "$meta": "vectorSearchScore" },
          },
        },
        {
          "$limit": limit,
        },
    ]
    results = collection.aggregate(pipeline)
    return list(results)