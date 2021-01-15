import requests
from bs4 import BeautifulSoup

# 1. url(주소)
url = 'https://finance.naver.com/sise/'

# 2. url로 요청을 보낸다.
response = requests.get(url).text

# 3. 받은 응답을 예쁘게 꾸며준다.
data = BeautifulSoup(response, 'html.parser')

# 4. 꾸민 응답 중에서 원하는 데이터 선택
result = data.select_one('#KOSPI_now').text
print(result)