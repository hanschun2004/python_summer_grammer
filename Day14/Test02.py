# 110p
# [문제 2]

# <출력>
# vector 수 : 3 
# 4
# 2
# 5
# vector 크기 : 3

# - vector 크기 입력
# - 크기 입력받은 만큼 반복 횟수 돌려준다
# - 반복문 안에서 랜덤값 봅는다.
# - 랜덤값 출력
# - 랜덤값을 list 안에 추가
# - 출력은 반복문 끝나고 리스트의 크기 출력
'''
ls = []
import random
# A형
vector = int(input("vector 수 : "))
for i in range(vector):
    rand = int(random.random()*vector) + 1
    print(rand)
    ls.append(rand)
print("vector 크기 : {}".format(len(ls)))
# B형
num = int(input())
if num in ls:
    print("YES")
if num not in ls:
    print("NO")

check = True
for i in ls: # i에는 리스트 안에 있는 값이 한개씩 대입한다.
    if i == num: # i의 값과 내가 입력한 값이 동일한지 확인 
        print("Yes") # 동일한게 참이면 YES 출력
        check = False # check를 False 로 바꾼다. 
if check: # check 가 True 일때만 실행 - 그렇기 때문에 check 가 False가 되면 No는 출력
    print("No")
'''
