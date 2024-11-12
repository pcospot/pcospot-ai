import os
from fastapi import APIRouter, HTTPException, Query
from dotenv import load_dotenv
import services.summarizeChat as sc
from pydantic import BaseModel

load_dotenv()

router = APIRouter(
    prefix="/summarize"
)

class ChatLog(BaseModel):
    chatLog: str

# post endpoint 사용한 이유 : 큰 사이즈의 채팅 데이터를 받아와야 하기에 body 데이터를 받을 수 있는 post method로 설정하였습니다.
@router.post('summarize')
async def search(chat: ChatLog) -> str:
    return sc.summarize(chat.chatLog) if chat else "채팅 데이터가 주어지지 않아 요약 데이터를 생성할 수 없어요."