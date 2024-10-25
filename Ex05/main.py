# 웹사이트용

import os  # os 모듈을 사용해서 환경변수에 접근
import sys
from openai import OpenAI
import chat_dao

sys.stdout.reconfigure(encoding="utf-8")

if len(sys.argv) > 1:
    question = sys.argv[1]

    # 컴퓨터의 한경변수의 키 값을 읽어 옴
    openai_api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=openai_api_key)

    # system 프롬프트
    prompt_txt = chat_dao.get_data()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "system",
                "content": prompt_txt,
            },
            {"role": "user", "content": question},
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={"type": "text"},
    )

    print(response.choices[0].message.content)
