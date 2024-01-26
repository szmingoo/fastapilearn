from fastapi import APIRouter
from fastapi import Body, FastAPI
from schemas import *
from typing import Set,Union

router = APIRouter()

# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None
#
# @router.post("/items6/{item_id}")
# async def update_item(item_id: int, user: User = Body(embed=True)):#嵌入单个请求体参数，入参为{“user”:{"username":"xx","full_name":"xx"}}
#     results = {"item_id": item_id, "user": user}
#     return results

class Model3(BaseModel):
    name: str
    price: float
    mtags: Set[str] = set()#mtags列表里面的value不重复
@router.put("/model3/{model_id}")
async def update_model(model_id: int, model: Model3):
    results = {"model_id": model_id, "model": model}
    return results


app=FastAPI()
app.include_router(router)
import uvicorn
uvicorn.run(host='localhost',port=8001,app=app)