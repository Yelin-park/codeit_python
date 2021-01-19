# key - value pari (키-값 쌍)
# 순서에 대한 개념이 없음. 사전의 키는 정수일 필요가 없음 문자도 가능.
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}

print(type(my_dictionary))

print(my_dictionary[3]) #키에 있는 값을 불러오는 법
my_dictionary[9] = 81 #키와 값을 추가하는 방법
print(my_dictionary)

my_famliy = {'엄마': '양성희',
             '아빠': '박문수',
             '딸': '박예린'}
print(my_famliy)

#사전 활용법
print(my_famliy.values()) #사전의 값
print('박예린' in  my_famliy.values()) #my_famliy 사전 안에 박예린 이라는 값이 있니?

for value in my_famliy.values(): #value 값을 반복적으로 출력하는 for문
    print(value)

print(my_famliy.keys()) #사전의 키
for key in my_famliy.keys(): #key 값을 반복적으로 출력하는 for문
    print(key)

for key in my_famliy.keys(): #key와 value 값을 반복적으로 출력하는 for문
    value = my_famliy[key]
    print(key, value)

for key, value in my_famliy.items(): #items를 활용하여 key와 value 값을 반복적으로 출력하는 for문
    print(key, value)