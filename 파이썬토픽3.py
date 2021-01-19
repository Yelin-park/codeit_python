# 리스트(list)
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

print(names)
print(numbers)

# 인덱싱 (indexing)
print(names[1])
print(names[0])
print(numbers[1] + numbers[3])
print(numbers[-2])

# 리스트 슬라이싱 (list slicing)
print(numbers[0:4]) #마지막 숫자는 -1이라는 것 꼭 기억하기 0부터3(1번째부터 3번째)
print(numbers[:3])

new_list = numbers[:3]
print(numbers[2])
numbers[0] = 7 #0번의 숫자를 7로 바꿈
print(numbers)

numbers[0] = numbers[0] + numbers[1]
print(numbers)

#리스트 함수
numbers = []
len(numbers) #리스트에 값이 몇 개가 있는지 알려주는 함수
print(len(numbers))

numbers.append(5) #리스트에 값을 추가하는 함수
numbers.append(8) #새로운 값을 오른쪽 끝에 추가함
print(numbers)
print(len(numbers))

new_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
del new_numbers[3] #리스트 안에 있는 값을 삭제하는 함수
print(new_numbers)

new_numbers.insert(4, 37) #원하는 위치에 새로운 값을 삽입하는 함수
print(new_numbers)

#리스트 정렬(sorted, sort)
#sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
#sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬

numbers_2 = [19, 13, 2, 5, 3, 11, 7, 17]

sorted(numbers_2) #리스트를 정렬시키는 함수, print 함수를 사용해여 출력가능
print(sorted(numbers_2))

new_list = sorted(numbers_2, reverse=True) #거꾸로 정렬하는 거 reverse=True
print(new_list) #숫자가 큰 순서대로 출력됨

print(numbers_2) #sorted는 기존의 리스트에 영향을 주지 않음

print(numbers_2.sort()) #기존의 리스트에 영향을 줌 print를 해도 값이 안나옴 정렬만 시켜주는 함수
print(numbers_2)

numbers_2.sort(reverse=True) #거꾸로 정렬
print(numbers_2)

#reverse 메소드(원소들을 뒤집어진 순서로 배치)
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)

#index 메소드(x의 값을 가지고 있는 원소의 인덱스를 보여줌)
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

#remove 메소드(첫 번째로 x의 값을 갖고 있는 원소를 삭제해줍니다.)
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)

#리스트 꿀팁
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)
print(7 not in primes)
print(12 not in primes)

#리스트 안에 리스트(다중 리스트)
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)


