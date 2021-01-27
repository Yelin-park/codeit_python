# 같은 폴더 안에 있어야 import로 불러올 수 있음
# as를 붙이고 불러올 이름을 지정할 수 있음
import calculator as calc

# calculator에서 add와 multiply 함수만 사용하겠다고 선언 따라서 calc를 쓰지 않고도 함수 사용 가능
from calculator import add, multiply

print(calc.add(2, 5))
print(calc.multiply(3, 4))
print(add(2, 5))
