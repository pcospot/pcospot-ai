from fastapi import APIRouter
from dotenv import load_dotenv
import services.sprint as sp

load_dotenv()

router = APIRouter(
    prefix="/sprint"
)

@router.get('/generate')
async def generate(startDate: str = "월", endDate: str = "금", subject: str = "", numOfPeople: str = "1명") -> str:
    return sp.generateSprint(startDate, endDate, subject, numOfPeople) if subject else "스프린트 주제가 주어지지 않아 생성할 수 없어요."

@router.get('/advice')
async def advice(elapsedDate: int, lastDate: int, sprintData: str) -> str:
    return sp.sprintSupport(elapsedDate, lastDate, sprintData) if elapsedDate and lastDate and sprintData else "필요 정보가 주어지지 않아 스프린트 조언을 제공할 수 없어요."