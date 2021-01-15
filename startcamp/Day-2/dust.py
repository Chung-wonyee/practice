import requests
from pprint import pprint

KEY = 'CY7i0PUjtXFUB09ieEB6CJnwmA9Fpzi0ps7OQnjg2%2Fdo5Yl6RMAO1kbqY4UlCigSPg7%2BqWTlh3fNgz1Ot2XZng%3D%3D'
return_type = 'json'
num_of_rows = '5'
page_no = '1'
sido_name = '서울'
ver = '1.0'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_name}&ver={ver}'

response = requests.get(url).json()
#pprint(response)

# stationName의 미세먼지 농도는 pm10value입니다. 라는 메세지를 출력
result_stationName = response['response']['body']['items'][0]['stationName']
result_pm10value = response['response']['body']['items'][0]['pm10Value']

#print(result_sidoName)
#print(result_pm10value)

print(f'{result_stationName}의 미세먼지 농도는 {result_pm10value}입니다.')