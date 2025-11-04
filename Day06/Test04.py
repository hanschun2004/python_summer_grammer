import random
# 1 ~ 100 까지 랜덤값을 출력하는 코드를 작성하세요
# (단, randint(), randrange()는 사용하지 않는다.)

# 100 ~ 999까지 랜덤값을 출력하는 코드를 작성하세요
# (단, randint(), randrange()는 사용하지 않는다.)

# 'A' ~ 'Z'까지 임의의 문자 3자리를 출력하는 코드를 작성하세요
# (단, randint(), randrange()는 사용하지 않는다.)

rand = int(random.random()*100) + 1
print(rand)

rand = int(random.random()*900) + 100
print(rand)

ch1 = chr(int(random.random()*26) + 65)
ch2 = chr(int(random.random()*26) + 65)
ch3 = chr(int(random.random()*26) + 65)
st = chr(int(random.random()*26) + 65) + chr(int(random.random()*26) + 65) + chr(int(random.random()*26) + 65)

print(ch1+ch2+ch3)
print(st)



