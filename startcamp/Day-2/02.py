# Dictionary (딕셔너리)

my_home = {                     # 딕셔너리는 순서가 없음!
    'location': 'SEOUL',        # 따라서 location은 첫번째라고 할 수 없다!
    'area-code': '02'
}

# 딕셔너리 원소 접근

# 1
print(my_home['location'])
# print(my_home['name'])#       # 없는 키 값 호출 시 KeyError

# 2
print(my_home.get('location'))
print(my_home.get('name'))      # 없는 키 값 호출 시 None