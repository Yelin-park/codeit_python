import random

random_number = random.randint(1, 20)

# 모범답안
# 상수 정의
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

# 변수 정의
guess = -1
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES - tries)))
    tries += 1
    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")
if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))


#다른 사람 코드
for i in range(0, 5):
    chance = 4 - i
    if chance == 0:
        print("아쉽습니다. 정답은 {}입니다.".format(str(random_number)))
        break
    number = int(input("기회가 {}번 남았습니다. 1-20사이의 숫자를 맞혀보세요: ".format(chance)))
    if number < random_number:
        print("UP")
    elif number > random_number:
        print("DOWN")
    elif number == random_number:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(chance))
        break








