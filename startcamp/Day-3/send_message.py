import requests

token = '1557387128:AAGYSbYfHhB0BC39kcPoUKKsZtl1Wz7-VHs'
app_url = f'https://api.telegram.org/bot{token}'

update_url = f'{app_url}/getUpdates'
response = requests.get(update_url).json()

chat_id = response.get('result')[0].get('message').get('from').get('id')

text = '방가방가'
message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)