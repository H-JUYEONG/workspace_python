# 1. 최소버전+토큰값
# 2. 이전 내용 기억하기
# 3. 사용자 질문 입력하기
# 4. 반복해서 질문 입력하기, 종료가능 (대화내용 누적)
# 5. 대화내용 누적 ---> 토큰(비용)을 많이 사용해야한다.

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

message_history = [
    {
        "role": "system",
        "content": prompt_txt,
    },
]


# 사용자로부터 질문입력 받기
print("***********************************")
print("***반갑습니다. 질문을 입력해주세요***\n")
print("***********************************")


while True:

    question = input("(사용자)")

    if question == "\q":
        break

    else:

        # 메세지
        message_history.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=message_history,
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={"type": "text"},
        )

        print(f"[챗_GPT]{response.choices[0].message.content}")
        message_history.append({"role": "assistant", "content": response.choices[0].message.content})


print("******************************************")
print("***갑사합니다. 이용해 주셔서 감사합니다.**")
print("******************************************")
