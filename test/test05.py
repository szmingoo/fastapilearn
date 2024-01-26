from fastapi import APIRouter,FastAPI
from pydantic import BaseModel, create_model

app=FastAPI()
router = APIRouter()

class User(BaseModel):
    name: str
    age: int

@router.post("/users/")
async def create_user(user: User):
    return {"user": user}

# 创建一个只读版本的User模型，用于docs中的request body
UserRead = create_model("UserRead", **{field: (type(value), ...) for field, value in User.__annotations__.items()})

@router.post("/users_read/")
async def create_user_read(user: UserRead):
    return {"user": user}

app.include_router(router)

import uvicorn
uvicorn.run(host='localhost',port=8011,app=app)