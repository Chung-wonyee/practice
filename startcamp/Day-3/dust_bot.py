import requests
from bs4 import BeautifulSoup


KEY = 'CY7i0PUjtXFUB09ieEB6CJnwmA9Fpzi0ps7OQnjg2%2Fdo5Yl6RMAO1kbqY4UlCigSPg7%2BqWTlh3fNgz1Ot2XZng%3D%3D'
URL = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=xml'

response = requests.get(URL).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[0]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')


# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
if dust > 150:
    status = '매우나쁨'
    print(status)
elif dust > 80:
    status = '나쁨'
    print(status)
elif dust > 30:
    status = '보통'
    print(status) 
else:
    status = '좋음'
    print(status)

token = '1557387128:AAGYSbYfHhB0BC39kcPoUKKsZtl1Wz7-VHs'
app_url = f'https://api.telegram.org/bot{token}'

update_url = f'{app_url}/getUpdates'
response = requests.get(update_url).json()

chat_id = response.get('result')[0].get('message').get('from').get('id')

text = f'{time} 기준 {station}의 미세먼지 농도는 {dust}으로 {status}상태 입니다.'
message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)