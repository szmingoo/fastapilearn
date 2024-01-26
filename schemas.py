from pydantic import BaseModel
from typing import List,Union

class Records(BaseModel):
    roleType:str
    content:str

class SummaryResquestModel(BaseModel):
    end_time: str
    dialogue: list[Records]=[]

class SummaryResponseModel(BaseModel):
    prompt:str
    code:int
    tokens:int


class FoctorResquestModel(BaseModel):
    dialogue: List

class FoctorResponseModel(BaseModel):
    personConcernStatus:str
    promiseAmount:str
    promiseRepayment:str
    nextCommunication:str


class FormatResquestModel(BaseModel):
    dialogue: List

class FormatResponseModel(BaseModel):
    agentMark:List
    mediatorMark:List
    otherMark:List