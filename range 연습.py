# range 연습

# 인덱스와 원소 출력
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for i in numbers:
    print(numbers.index(i), i)

# 2의 n제곱을 출력하는 프로그램
for i in range(11):
    print("2^{} =".format(i), 2**i)

# 구구단 프로그램(for문 사용)
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)

# 피타고라스 삼조 (a^2 + b^2 = c^2을 만족하는 세 자연수 쌍(a,b,c))
# a < b < c라고 가정할 때, a+b+c=1000을 만족하는 경우
for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c and a < b < c and a + b + c == 1000:
            print(a * b * c)

#리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

temp = []
for i in range(8):
    x = numbers[i]
    temp.insert(0, x)
numbers = temp
print("뒤집어진 리스트: " + str(numbers))

#모범답안
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers) // 2): # len(numbers)//2 = 4
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1
    # 8 - 0 - 1 = 7
    # 8 - 1 - 1 = 6
    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]
    # numbers[7], numbers[0] = numbers[0], numbers[7]
    # numbers[6], numbers[1] = numbers[1], numbers[6]

print("뒤집어진 리스트: " + str(numbers))