with open('data/chicken.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        print(line.strip())

# strip : 화이트 스페이스(공백)을 제거해 줌
print("     abc     def".strip())
print(" \t    \n    abc     def\n\n\n".strip())


# 중간 공백 제거하는 방법 : replace 메소드 활용
message = "   코     드   잇"
new_message = message.replace(" ", "")
print(new_message)

# split : 어떠한 기준으로 문자를 나눠주는 것
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split('. ')) # '. '를 기준으로 문자를 나눠줌

full_name = "Kim, Yuna"
print(full_name.split(','))
print(full_name.split(', '))

name_data = full_name.split(', ')
last_name = name_data[0]
first_name = name_data[1]
print(first_name, last_name)

print("   \n\n   2   \t   3  \n 5 7 11   \n\n".split()) #화이트 스페이스는 사라지고 문자만 나옴
numbers = "   \n\n   2   \t   3  \n 5 7 11   \n\n".split()
print(numbers[0] + numbers[1]) #split은 문자열이기 때문에 문자열 연산이 됨
print(int(numbers[0]) + int(numbers[1])) # 자료형을 숫자로 바꾸고 연산을 하면 숫자 연산이 가능

