import os
import requests
from main import client

db_name = os.getenv('DATABASE_NAME')
collection_name = os.getenv('COLLECTION_NAME')
openai_key = os.getenv("OPENAI_KEY")

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

async def search(word: str, limit: int):
    queryVector = await getEmbedding(word)
    pipeline = [
        {
          "$vectorSearch": {
            "queryVector": queryVector,
            "path": "vectorEmbedding",
            "numCandidates": 100,
            "exact": False,
            "limit": 30,
            "index": "subsidy_vector_index",
          },
        },
        {
          "$project": {
            "_id": 0,
            "articleId": 1,
            "articleTitle": 1,
            "score": { "$meta": "vectorSearchScore" },
          },
        },
        {
          "$limit": 30,
        },
      ]