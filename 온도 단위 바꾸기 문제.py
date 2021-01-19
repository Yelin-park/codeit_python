#화씨 온도를 섭씨 온도로 바꾸어주는 프로그램
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
celsius_list = []
celsius_list.append(round(fahrenheit_to_celsius(temperature_list[0]),1))
celsius_list.append(round(fahrenheit_to_celsius(temperature_list[1]),1))
celsius_list.append(round(fahrenheit_to_celsius(temperature_list[2]),1))
celsius_list.append(round(fahrenheit_to_celsius(temperature_list[3]),1))
celsius_list.append(round(fahrenheit_to_celsius(temperature_list[4]),1))
celsius_list.append(round(fahrenheit_to_celsius(temperature_list[5]),1))

print("섭씨 온도 리스트: " + str(celsius_list))  # 섭씨 온도 출력



#모범 답안
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드
i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1
print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력
