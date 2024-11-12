import os, uvicorn, dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import pymongo
from controllers import search, sprint, summarize

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

app.include_router(search.router)
app.include_router(sprint.router)
app.include_router(summarize.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)