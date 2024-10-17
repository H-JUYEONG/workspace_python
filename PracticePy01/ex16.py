# 주어진 문자열의 공백을 ‘,’(콤마) 로 변경 후 출력하세요.
# ['T','h','i','s',' ','i','s',' ','a',' ','p','e','n','c','i','l']


list = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'p', 'e', 'n', 'c', 'i', 'l']

# 리스트를 하나의 문자열로 합치기
sentence = ''.join(list)

modified_sentence = sentence.replace(' ', ',')

print(sentence) 
print(modified_sentence)
