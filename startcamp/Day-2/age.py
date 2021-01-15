import requests

name = input()

url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()

name = response['name']
age = response['age']
count = response['count']

print(f'{name}의 나이는 {age}입니다.')