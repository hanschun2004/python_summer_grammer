import random

# randrange(n,m,p)
# 범위안의 임의의 정수값을 구하는 함수
# n~m 미만
# p는 생략가능 ..p 만큼 증가한 값들 중에

rand = random.randrange(1,2) # 1 ~ 2 미만
print(rand)

rand = random.randrange(2) # 0 ~ 2미만.. 0은 생략 가능
print(rand)

rand = random.randrange(0,10,2) # 0 ~ 10 미만까지 2 씩 증가한 값들 중 
print(rand) # 0 2 4 6 8 



































