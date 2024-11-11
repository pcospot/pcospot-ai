import os, requests
from openai import OpenAI

lm_api = os.getenv("LM_API_URI")
model_id = os.getenv("MODEL_ID")

client = OpenAI(
    base_url=f"{lm_api}/v1",
    api_key="apikey"
)

# 요일, 주제(할 일: ex 게시판 생성 등)를 전달받아 생성
def generateSprint(startDate: str, endDate: str, subject: str, numOfPeople: str) -> str:
    try:
        completion = client.chat.completions.create(
            model=f"{model_id}",
            messages=[
                {"role": "system", "content": "너는 스프린트 일정을 만드는 AI야. 너에게는 시작 요일, 종료 요일, 스프린트 주제, 인원 수가 주어져."},
                {"role": "user", "content": f"시작 요일은 {startDate}이고, 종료 요일은 {endDate}, 참여 인원은 {numOfPeople}이야. 스프린트 주제는 {subject}야. 요일별 스프린트를 작성해줘."}
            ],
            temperature=0.6
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise e
    
# 스프린트 감독 AI : 지금까지 스프린트 잘 하고 있는지 : 정확히는 조언하는 기능
# parameter로 스프린트 시작 후 경과일, 스프린트 관련 정보를 입력받습니다.
def sprintSupport(elapsedDate: int, lastDate: int, sprintData: str) -> str:
    try:
        completion = client.chat.completions.create(
            model=f"{model_id}",
            messages=[
                {"role": "system", "content": "너는 한 조직의 스프린트 감독관이야. 주어진 스프린트 상황에 맞는 피드백을 단 한 줄로 해야 해. 잊지 마. 단 한 줄로 작성해야 해."},
                {"role": "user", "content": f"스프린트 시작 후 경과일: {elapsedDate}일, 잔여 기간: {lastDate}일, 스프린트 정보: {sprintData}. "}
            ],
            temperature=0.6
        )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content
    except Exception as e:
        raise e