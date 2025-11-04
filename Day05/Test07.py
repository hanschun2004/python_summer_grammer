# 모듈
# 어떠한 기능들이 정의 되어 있는것
# 파이선에서는 웬만한 기능들은 모두 정의 되어있다.
# 기능을 사용하려면 모듈을 지정하여 불러와서 사용하면 된다.

# 형식
# from 모듈명 import 함수명
# 모듈안에 있는 일부 기능을 사용하기 위한 형식
# import 모듈명
# 모듈 전체

# random 모듈 - 임의의 수를 구하는 함수들이 정의된 모듈
# from random import random
# import random

# 임의의 수 구하기
# random()
# 0 ~ 1미만의 실수를 구하는 함수
# 0.0000 ~ 0.9999

# 내가 원하는 범위안의 수를 구하기
# int(random.random() * 범위 안의 수의 개수 ) + 시작수
# int(random() * 범위 안의 수의 개수) + 시작수

# 20 ~ 24  : 총 5개

'''import random
ran = int(random.random()*5) + 20

a = random.random() # 0.0000 ~ 0.9999
b = a * 5 # 0.0000 ~ 4.9999
c = int(b) # 0 ~ 4
d = c + 20 # 20 ~ 24
# print(d , ran)
print(a)
print(b)
print(c)
print(d) '''

from random import random
# 1 ~ 10
ran = int(random()*10) + 1
print(ran)

# 2 ~ 20
ran = int(random() * 19) + 2   # 19개 수!!! + 시작수 
print(ran)










































