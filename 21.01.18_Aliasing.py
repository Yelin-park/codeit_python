x = [2, 3, 5, 7, 11]
y = x #같은 리스트를 사용하게 되어서
y[2] = 4 #값을 바꾸어줘도
print(x) #x와 y는 같은 값이 나오게 됨
print(y)

x = [2, 3, 5, 7, 11]
y = list(x) #list x를 복사해 y에 입력
y[2] = 4 #따라서 y의 값을 바꿔주면
print(x) #x와 y가 출력되는 리스트는 다름
print(y)


x = [2, 3, 5, 7, 11]
y = list(x) #list x를 복사해 y에 입력
z = x

x[0] = 10
y[1] = 8
z[3] = 17
print(x)


for i in range(10):
    print(i)

