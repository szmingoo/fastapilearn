from http import HTTPStatus
import dashscope

dashscope.api_key="sk-115a76a9850a4b40812cb9a9be093a4b"

def tokenizer():
    response = dashscope.Tokenization.call(model='qwen-plus',
                                 messages=[{'role': 'user', 'content': '你好？'}],
                                 )
    if response.status_code == HTTPStatus.OK:
        print('Result is: %s' % response)
    else:
        print('Failed request_id: %s, status_code: %s, code: %s, message:%s' %
              (response.request_id, response.status_code, response.code,
               response.message))


if __name__ == '__main__':
    tokenizer()