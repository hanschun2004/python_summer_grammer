# 나이를 저장하는 변수 선언과 초기화
age = 20
# 변수명 : age
# 초기화 : 20
print("age = {}".format(age)) # 변수의 호출

height = 177.2
print("height : {:.1f}".format(height))

age = 15 # 초기화 X 선언 X , 변수의 값 변경 O
print("age = {}".format(age))

# type()
# -Data Type 을 알려주는 함수
print(type(10))
print(type(age))
print(type("10"))
print(type(height))
print(type(True))

# 작명 규칙
# 1a = 20 - 변수명은 숫자로 시작 X    a1 = 20 O

import keyword
print(keyword.kwlist) # 예약어는 변수명으로 사용 불가능
AGE = 40
print(age, AGE)


