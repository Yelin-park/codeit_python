# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)
    for digit in str_num:
        total += int(digit)
    return total

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
i = 0
sum_total = 0
for i in range(1001):
    sum_total += sum_digit(i)
print(sum_total)


def sum_digit(num):
    total = 0
    str_num = str(num)

    for i in range(len(str_num)):
        digit = str_num[i]
        total += int(digit)

    return total