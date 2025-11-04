# 문자열에서 사용되는 함수

msg = "                   abcdefghijklmnopqra              "

# find(str)
# 문자열에서 특정 문자열 찾아 해당하는 문자의 인덱스 값을 반환하는 함수
# 없으면 -1을 반환 , 있으면 인덱스 값을 반환

print(msg.find("fghi"))
print(msg.find("c"))
print(msg.find("가"))

# count(str)
# 문자열에서 특정 문자열을 찾아서 해당 문자열의 수를 반환하는 함수

print(msg.count("a"))
print(msg.count("가"))

# lower() - 대문자를 소문자로 변환
# upper() - 소문자를 대문자로 변환
# swapcase() - 소문자는 대문자로 , 대문자는 소문자로 변환

s = "AbCdef"
print(s.lower())
print(s.upper())
print(s.swapcase())

# islower() - 문자열이 전부 소문자면 True
# isupper() - 문자열이 전부 대문자면 True

print(s.islower())
print(s.isupper())

# s라는 변수에 있는 문자열에 islower()을 사용하면 True라는 값이
# 나올 수 있도록 작성해보세요

print(s.lower().islower())
s = s.lower()
print(s.lower())

# 공백 제거 함수
# strip() - 앞 뒤 제거
# lstrip() - 좌측 제거
# rstrip() - 우측 제거

print(msg.strip())
print(msg.rstrip())
print(msg.lstrip())

# replace(old, new)
# old 문자열을 new문자열로 치환하는 함수

print(msg.replace("ab","가나"))

# split(str)
# 문자열을 특정 문자열을 기준으로 분리하는 함수
msg = "빨-주-노/초-파/남-보"
print(msg.split("-"))
print(msg.split("/"))
a = msg.split("-") 
print(a[2].split("/")) #"노/초"



































