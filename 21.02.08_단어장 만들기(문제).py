with open('vocabulary.txt', 'a', encoding='utf-8') as v:
    while True:
        eng = input('영어 단어를 입력하세요: ')
        if eng == 'q':
            break

        kor = input('한국어 뜻을 입력하세요: ')
        if kor == 'q':
            break

        v.write('{}: {}\n'.format(eng, kor))

#while True는 무한반복이다. if문을 사용해 break가 있어서 멈출 수 있다.



