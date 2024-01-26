from fastapi import FastAPI
from agency.mediate_disputes import router as cr_router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(cr_router)


import uvicorn
uvicorn.run(host='localhost',port=8001,app=app)