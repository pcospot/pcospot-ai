import os, pymongo, sys
sys.path.append("./src")
import services.vectorSearch as vectorSearch

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

response = vectorSearch.getEmbedding("apple")
print(response)