with open('data/vocabulary.txt', 'r', encoding='utf-8') as v:
    while True:
        for line in v:
            ans = input("{}: ".format(line.strip().split(':')[1]))
            if ans == line.strip().split(':')[0]:
                print("맞았습니다!")
            else:
                print("아쉽습니다. 정답은 {}입니다.".format(line.strip().split(':')[0]))


# 모범답안
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]

        # 유저 입력값 받기
        guess = input("{}: ".format(korean_word))

        # 정답 확인하기
        if guess == english_word:
            print("정답입니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))