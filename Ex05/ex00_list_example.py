message_history = ["system"]


message_history.append("질문1")
message_history.append("대답1")

message_history.append("질문2")
message_history.append("대답2")

message_history.append("질문3")
message_history.append("대답3")

message_history.append("질문4")
message_history.append("대답4")

print(message_history)
print("-------------------------")
print(message_history[0])  # 글자
print(message_history[-4:])  # 4개짜리 배열

print([message_history[0]] + message_history[-4:])
