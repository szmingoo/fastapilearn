from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

class Dialogue(BaseModel):
    roleType: str
    content: str

class InputData(BaseModel):
    end_time: int
    dialogue: List[Dialogue]

@app.post("/process_data/")
async def process_data(request: InputData):
    # data = await request.json()
    # input_data = InputData(**data)
    # 在这里处理输入数据，例如保存到数据库或执行其他操作
    return request

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8004)