# 리스트(list) 사용
stores = ['새마을식당', '리춘시장', '스타벅스']
print(stores)
print(stores[1])

# random 모듈 및 sample 함수 사용
import random

pick = random.sample(stores, 1)
print(pick)