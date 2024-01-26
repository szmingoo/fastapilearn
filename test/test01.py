from urllib.parse import quote
from fastapi import FastAPI,Query,Path,Header,Body
from fastapi.exceptions import RequestValidationError
from httpcore import Request
from pydantic import BaseModel, Field
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from starlette.responses import HTMLResponse, Response

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class JPGError(Exception):pass

@app.exception_handler(RequestValidationError)
async def custor_error(request:Request,error):
    error={
        'value_error.missing':'必填项',
        'type_error.integer':'字段内容必须是数值',
        'value_error.str.regex':"字段的数据不合法",
        'value.error.number.not_ge':"数值太低",#not_gt\le\lt
        'value.error.any_str.min_length':f"字符长度不足",
    }


@app.get('/')
async def root():
    return {"message":"hello,word"}

# uvicorn one_fastapi --reload
# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/docs

class LoginUser(BaseModel):
    name:str
    is_save:bool=False

@app.post('/login')
def user_login(user:LoginUser):
    raise HTTPException(status_code=404,detail={"msg":quote("发生错误")})

@app.get('/login')#/login?name=disen&pwd=123
def user_login_get(name:Query(...,min_length=8,max_length=20,regex=r'^[a-zA-Z]+$')):pass

@app.get('/active/{user_id}')#/active/2
def active_login_get(request:Request,user_id:int=Path(...,ge=1)):
    html=f'''<h1>请求的资源不存在:{request.url}</h1>'''
    return HTMLResponse(html,status_code=404)

class UserInfo(BaseModel):
    nick_name:Optional[str]=Field(None,max_length=20,regex=r'[\u4e00-\u9fa5]+',title='中文')

@app.put('/user',description='更新用户',name='更新用户')
def update_user(token:Optional[str]=Header(max_length=32,alias='Authorization'),user:UserInfo=Body(...)):
    return JSONResponse({"msg":"ok"})


#请求之前，实现权限验证，数据换成和节流（限制单IP的1秒内的请求次数）以及用户行为手机（数据分析）
#响应之前，增加header信息
@app.middleware('http')
async def looger_handler(request:Request,next_call):
    #请求之前
    resp:Response=next_call(request)
    return resp

import uvicorn
uvicorn.run(host='localhost',port=8001,app=app)