import os
from pathlib import Path
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="fable",
    input="집에 가고싶다. 눕고싶다. 오늘은 왜 월요일인가?",
    response_format="mp3",
    speed=0.8
)

speech_file_path = "C:\\javaStudy\\workspace_python\\Ex05\\tts.mp3"
with open(speech_file_path, "wb") as file:
    file.write(response.content)
    # 알아서 file.close() --> with 문법