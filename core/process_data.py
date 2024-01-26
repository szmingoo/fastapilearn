import re
from typing import List, Dict,Tuple
import jieba

STOP_WORDS = ['喂', '啊', '呃', '嘛', '哎', '的话', '那个']
CUSTOM_DICT = ['知道了', '好的', '了解了', '对了', '行吧']

def is_chinese_date(text: str) -> bool:
    chinese_date_pattern = re.compile(r'\d{4}年\d{1,2}月\d{1,2}日')
    return bool(chinese_date_pattern.search(text))

def is_english_date(text: str) -> bool:
    english_date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    return bool(english_date_pattern.search(text))

def is_number(text: str) -> bool:
    number_pattern = re.compile(r'^[-+]?\d+(\.\d+)?$')
    return bool(number_pattern.match(text))

# 对每个content进行去重、停用词清洗等处理
def clean_content(content: str) -> str:
    content = re.sub(r"[\s+!/_,$%^*(+\''\)：+——()?【】“”！，。？、~@#￥%……&*（）]+", '', content)
    tokens = [word for word in jieba.cut(content) if word not in STOP_WORDS]
    for word in CUSTOM_DICT:
        jieba.add_word(word)

    unique_tokens = []
    previous_token = None
    for current_token in tokens:
        if (is_chinese_date(current_token) or is_english_date(current_token) or
            is_number(current_token)):
            unique_tokens.append(current_token)
        elif current_token != previous_token:
            unique_tokens.append(current_token)
        previous_token = current_token

    return ''.join(unique_tokens)

# 对入参对话进行处理
def process_dialogue(order: Dict) -> Tuple[str, List[Dict], str]:
    '''order:'''
    if isinstance(order, dict):
        processed_dialogue = []

        for item in order.get('dialogue', []):
            role_type = item.get('roleType')
            content = clean_content(item.get('content', ''))
            if content:
                if processed_dialogue and processed_dialogue[-1].get('roleType') == role_type:
                    processed_dialogue[-1]['content'] = \
                        clean_content(processed_dialogue[-1]['content'] + content)
                else:
                    processed_item = {'roleType': role_type, 'content': content}
                    processed_dialogue.append(processed_item)

        merged_dialogue = '\n'.join([
            f"{item['roleType'].replace('AGENT', '调解员').replace('CUSTOMER', '当事人')}: {item['content']}"
            for item in processed_dialogue
        ])

        return order.get('end_time'), processed_dialogue, merged_dialogue