from starlette.responses import JSONResponse
from fastapi import APIRouter, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from schemas import *
from core import process_data, generate_abstract

router = APIRouter()

@router.post("/agency/v1/summary",tags=["沟通记录摘要"],name='沟通记录摘要',response_model=SummaryResponseModel)
async def chat_processed(summary:SummaryResquestModel) -> JSONResponse:
    try:
        data = jsonable_encoder(summary)
        end_time, processed_dialogue, merged_dialogue = process_data.process_dialogue(data)
        prompt = generate_abstract.prompt_template(merged_dialogue)
        cost_token = generate_abstract.calculate_token(prompt=prompt)
        if cost_token>30000:
            prompt = generate_abstract.prompt_template(merged_dialogue[:-29000])
            cost_token = generate_abstract.calculate_token(prompt=prompt)
        return JSONResponse({"prompt": prompt, 'code': 200,'tokens':cost_token,'processed_dialogue':merged_dialogue})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("agency/v1/factor",tags=["提取沟通要素"],name='提取沟通要素',response_model=FoctorResponseModel)
async def chat_foctor(foctor:FoctorResquestModel)->JSONResponse:
    """提取要素"""
    try:
        data = foctor.dict()
        #此处调用算法核心层
        return JSONResponse(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("agency/v1/format",tags=["区分角色"],name='区分角色',response_model=FormatResponseModel)
async def chat_format(format:FormatResquestModel)->JSONResponse:
    """区分角色"""
    try:
        data = format.dict()
        # 此处调用算法核心层
        return JSONResponse(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))