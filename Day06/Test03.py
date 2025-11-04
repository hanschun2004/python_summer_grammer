# 문자 체계
# 문자를 처리하기 위해서 문자마다 고유한 정수값을 정해놓은 체계
# 아스키 코드 : C 계열의 언어
# 0 ~ 127 까지의 문자를 처리하는 문자 체계
# 알파벳, 숫자, 특수기호, 제어문자 등의 키보드 위에 문자들
# 키보드의 키값
# 유니코드 : 파이썬 , JAVA
# 아스키코드 + 이세상의 모든 문자 = 약 6만개
# 오늘날에 가장 널리 쓰이는 문자 체계

# 형변환 함수
# 문자변환 함수 - chr(정수)
# 문자 -> 정수 - ord(문자)
print(chr(65))
print(chr(92))
print(chr(95))


print(ord('가'))
print(chr(44032))
print(ord('나'))
print(chr(45208))

# 대문자 영어, 소문자 영어가 랜덤으로 나올 수 있도록

# 1) 대문자 # 65 ~ 90
import random
rand = int(random.random()*26) + 65
print(chr(rand))


# 2) 소문자 # 97 ~ 122
rand = random.randint(97,122)
print(chr(rand))


'''
import random
cap = random.randrange(65,90)
print(chr(cap))
small = random.randrange(97,122)
print(chr(small))
'''





































