with open('data\chicken.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        data = line.strip().split(': ')
        total = int(data[1])
print(sum(total))

