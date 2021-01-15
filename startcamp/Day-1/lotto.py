import random

# 1. 1 부터 45 까지의 수
numbers = range(1, 46)

# 2. 6 개를 무작위로 추첨
pick = random.sample(numbers, 6)

print(pick)

# string-interpolation (보간법) - stirng 사이에 값을 삽입
# f-string
print(f'오늘의 로또 번호는 {pick} 입니다.')