# 1. 단어장 만들기
vocab = {'sanitizer': '살균제',
         'ambition': '야망',
         'conscience': '양심',
         'civilization':'문명'
         }
print(vocab)

# 2. 새로운 단어들 추가
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'

print(vocab)


#사전 뒤집기(한영사전)
# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict  # 변환한 새로운 사전 리턴



#for key in my_famliy.keys(): #key와 value 값을 반복적으로 출력하는 for문
    #value = my_famliy[key]
    #print(key, value)

#for key, value in my_famliy.items(): #items를 활용하여 key와 value 값을 반복적으로 출력하는 for문
    #print(key, value)

# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))