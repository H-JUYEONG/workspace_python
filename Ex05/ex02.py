# 1. 최소버전+토큰값
# 2. 이전 내용 기억하기

import os  # os 모듈을 사용해서 환경변수에 접근
from openai import OpenAI

# 컴퓨터의 한경변수의 키 값을 읽어 옴
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

# system 프롬프트
prompt_txt = """
    #context
    100 글자 이내로 답해주세요

    # tone
    친절한 말투로 답변해주세요
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {
            "role": "system",
            "content": prompt_txt,
        },
        {"role": "user", "content": "제이름은 황일영입니다."},
        {"role": "assistant", "content": "황일영님 반갑습니다."},
        {"role": "user", "content": "대한민국의 수도는?"},
        {
            "role": "assistant",
            "content": "대한민국의 수도는 서울입니다. 혹시 더 궁금한 사항이 있으시면 언제든지 물어보세요",
        },
        {"role": "user", "content": "그곳의 인구 수는?"},
        {"role": "assistant", "content": "1000만명 입니다."},
        {"role": "user", "content": "내이름은?"},
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={"type": "text"},
)

print(response.choices[0].message.content)
