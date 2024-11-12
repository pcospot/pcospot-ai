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
    import services.summarizeChat as sc
    sc.summarize("""[백엔드] 정은수 - 어제 오후 11:10
@[프론트] 신유준 백엔 Unstable 보고 먼저 개발좀 해주세요
@[프론트] 신유준
[프론트] 신유준 - 어제 오후 11:16
넴
[백엔드] 정은수 - 어제 오후 11:16
혹시 Socket.io 사용하실 수 있으신가요?
Socket.IO
[프론트] 신유준 - 어제 오후 11:16
아니오
[백엔드] 정은수 - 어제 오후 11:18
그러면
WebSocket
사용하실수 있으신가요
[프론트] 신유준 - 어제 오후 11:20
ㅇㅏ니오
[백엔드] 정은수 - 어제 오후 11:20
?
[프론트] 신유준 - 어제 오후 11:20
한다면 할수는 있습니다
[AI] 이주안 - 어제 오후 11:21
claude 등 ai 다 가져다쓰고
ai가 만든 흔적 (ex 주석)만 다 지웁시다
[백엔드] 정은수 - 어제 오후 11:22
그러면 Socket.io 씁시다
확실히 websocket으로 시작하는것보단
socketio가 낫죠
[AI] 이주안 - 어제 오후 11:25
@everyone 여러분들 저희 보고서에 넣을 각자 사진 필요합니다. 내일 오전 9시까지 @[AI] 이주안 DM으로 보내주세요.
주현명 - 어제 오후 11:27
SocketIO
가 더 나은 이유가 뭔가요
[백엔드] 정은수 - 어제 오후 11:40
초보자에게
조금 더 편하지 않을까요
깡 웹소켓보단
둘다 모른다고하니..
거기다가 시간도 촉박하니
지금으로선 최적인거같아요
주현명 - 어제 오후 11:41
초보자에게 편하다는건 무슨 의미죠
[백엔드] 정은수 - 어제 오후 11:41
음
약간 채널기능 있고
막 그런게 있는게
더 편하다고 느끼지 않을까요
혹시 쓰지 말아야할 이유가 있을까요
이유가 있다면 다른 것을 채택하는것도 고려해볼만 하다고 생각합니다
제 입장에서는 깡 웹소켓 쓰는것 보단 편했었어서
채택한것입니다
아 그리고 웹소켓이라는 것을 이용하는 이유가
https://discord.com/blog/how-discord-reduced-websocket-traffic-by-40-percent
How Discord Reduced Websocket Traffic by 40%
때문 입니다
의견 있으시면 편하게 말씀 부탁드립니다
제가 사람인지라 트렌드를 다 따라가기 힘들어서
요즘 프론트엔드쪽에서는 어떤걸 사용하는지 업데이트가 되지않았네요
주현명 - 오늘 오전 12:00
딱히 트렌드에 맞춰가지는 않는데요
SoketIO가 여러 기술을 더 쓰기 편하게 만든 라이브러리인건 맞죠
모든 통신을 소켓으로 처리할 생각이신가요
[백엔드] 정은수 - 오늘 오전 12:10
아뇨
모든통신을 소켓으로 굳이..처리할 필요는 없다고 생각합니다
실시간 채팅부분만 소켓으로 처리할 생각이였습니다""")
    uvicorn.run(app, host="0.0.0.0", port=9000)