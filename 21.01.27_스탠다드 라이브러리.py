# standard library (표준 라이브러리)

import math

print(math.log(10))
print(math.cos(0))
print(math.pi)


import random

#0.0~1.0 사이의 랜덤 수를 줌
print( random.random())
#1과 20 사이에 만족하는 어떤 랜덤한 정수 N을 리턴
print(random.randint(1, 20))
#0과 1 사이에 만족하는 어떤 랜덤한 소수 N을 리턴
print(random.uniform(0, 1))


import os

#현재 컴퓨터에 어떠한 계정으로 로그인 되어있는지 알려줌
print(os.getlogin())
print(os.getcwd())


import datetime

pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))

#날짜와 시간까지 설정
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))

#오늘 날짜
today = datetime.datetime.now()
print(today)
print(type(today))

#timedelta : datetime 값 사이의 기간을 알고 싶으면 뺄셈을 하듯이 빼면 됨
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day)) #<class 'datetime.timedelta'> : 날짜 간의 차이를 나타내는 타입

#timedelta를 생성해서 datetime 값에 더해줄 수도 있음
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
#5일 3시간 10분 50초 후의 날짜를 계산해줌
print(today + my_timedelta)

#datetime 해부하기
today = datetime.datetime.now()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)
print(today.microsecond)

#datetime 포맷팅 : strftime을 사용

today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))

#포맷 코드
#%a	요일 (짧은 버전)	Mon
#%A	요일 (풀 버전)	Monday
#%w	요일 (숫자 버전, 0~6, 0이 일요일)	5
#%d	일 (01~31)	23
#%b	월 (짧은 버전)	Nov
#%B	월 (풀 버전)	November
#%m	월 (숫자 버전, 01~12)	10
#%y	연도 (짧은 버전)	16
#%Y	연도 (풀 버전)	2016
#%H	시간 (00~23)	14
#%I	시간 (00~12)	10
#%p	AM/PM	AM
#%M	분 (00~59)	34
#%S	초 (00~59)	12
#%f	마이크로초 (000000~999999)	413215
#%Z	표준시간대	PST
#%j	1년 중 며칠째인지 (001~366)	162
#%U	1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
#%W	1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35