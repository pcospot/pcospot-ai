import os, requests
from openai import OpenAI

lm_api = os.getenv("LM_API_URI")
model_id = os.getenv("MODEL_ID")

client = OpenAI(
    base_url=f"{lm_api}/v1",
    api_key="apikey"
)

# 요일, 주제(할 일: ex 게시판 생성 등)를 전달받아 생성
def generateSprint(startDate: str, endDate: str, subject: str):
    try:
        completion = client.chat.completions.create(
            model=f"{model_id}",
            messages=[
                {"role": "system", "content": "Always answer in rhymes."},
                {"role": "user", "content": "Introduce yourself."}
            ],
            temperature=0.6
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise e