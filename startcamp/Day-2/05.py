# 조건문

# 1. 주어진 양수 n이 홀수, 짝수인지 판별하여 출력
n = int(input())

if(n % 2 == 0):
    print('짝수')
else:
    print('홀수')






# 반복문

# 리스트의 원소 중에서 홀수만 찾아 그 값을 '~ 는 홀수입니다.' 라고 출력
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number % 2 == 1:
        print(f'{number}(은)는 홀수입니다.')