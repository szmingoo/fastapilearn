from http import HTTPStatus
import dashscope
import os
from utils.ini_opt import ReadConfig
from dotenv import load_dotenv, find_dotenv

rc=ReadConfig()
model_version=rc.get_model_version()
api_key=rc.get_model_api_key()

# _ = load_dotenv(find_dotenv())
# model_version=os.getenv("MODEL_VERSION")
# api_key=os.getenv("API_KEY")

dashscope.api_key=api_key


# 生成prompt
def prompt_template(combine_record: str) -> str:
    # TODO: model和prompt还需优化
    prompt = f"""{combine_record}
为以上对话内容写一篇摘要，具体要求如下：
1. 使用通俗易懂的语言撰写摘要
2. 摘要应包括一个小结和一个相关要点的列表
3. 输出必须是中文"""
    return prompt

# 计算token数 【输出的token数需再次调用计算】
def calculate_token(prompt: str) -> int:
    # response = dashscope.Tokenization.call(model=model_version,messages=[{'role': 'user', 'content': prompt}])
    # if response.status_code == HTTPStatus.OK:
    #     return response.usage.get('input_tokens', -1)
    # return -1
    return 3