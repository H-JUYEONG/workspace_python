import os
from pathlib import Path
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

# 파일 불러오기
file_path = "C:\\javaStudy\\prompt.txt"

with open(file_path, "r", encoding="UTF-8") as file:
    data = file.read()

# 사용자 입력
print("*****주제를 입력해주세요*****")
title = input("주제: ")

prompt_txt = data

message_history = [
    {
        "role": "system",
        "content": prompt_txt,
    },
    {"role": "user", "content": title},
]

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

ai_txt = response.choices[0].message.content
print(response.choices[0].message.content)

speech_file_path = Path("C:\\javaStudy\\poem.mp3")
response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=ai_txt,
    response_format="mp3",
    speed=1.0,
)

with open(speech_file_path, "wb") as file:
    file.write(response.content)
