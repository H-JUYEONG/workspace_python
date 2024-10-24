# 1. 최소버전+토큰값

import os  # os 모듈을 사용해서 환경변수에 접근
from openai import OpenAI

# 컴퓨터의 한경변수의 키 값을 읽어 옴
openai_api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {
            "role": "system",
            "content": "너는 일반적인 문장을 시로 표현을 잘하는 재능을 가진 유명한 시인이야",
        },
        {"role": "user", "content": "자바의 역사를 200자 이내로 표현해줘"},
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={"type": "text"},
)

print(response.choices[0].message.content)


# 토큰 수 확인
q_token = response.usage.prompt_tokens  # 질문 토큰수
a_token = response.usage.completion_tokens  # 응답 토큰수
t_token = response.usage.total_tokens  # 전체 토큰수
print(f"질문:{q_token} + 응답:{a_token} = 합계:{t_token}")
