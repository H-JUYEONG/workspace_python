import os
from openai import OpenAI

openai_api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key = openai_api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {
            "role": "system",
            "content": "너는 일반적인 문장을 시로 표현을 잘하는 재능을 가진 유명한 시인이야",
        },
        {"role": "user", "content": "자바의 리스트를 200자 이내로 표현해줘"},
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={"type": "text"},
)

print(response.choices[0].message.content)
