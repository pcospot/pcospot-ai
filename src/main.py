import os, uvicorn, dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import pymongo

dotenv.load_dotenv()

global client
client = pymongo.MongoClient(os.getenv('MONGO_URI'))

app = FastAPI(
    title="pcospot-ai",
    description="pcospot ai",
    version="dev",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import services.vectorSearch as vs
    r = vs.getEmbedding("apple")
    uvicorn.run(app, host="0.0.0.0", port=9000)