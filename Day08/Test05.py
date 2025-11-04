# 업다운 게임을 구현하려 합니다
# 컴퓨터에게 1부터 100사이의 정답을 생성하도록 코드를 구현한 뒤
# 사용자가 숫자를 입력하여 정답을 맞추도록 프로그래밍 하세요

# 게임상태
# [업] 사용자가 정답보다 낮은 값을 입력한 경우
# [다운] 사용자가 정답보다 높은 값을 입력한 경우
# [정답] 사용자가 정답과 같은 값을 입력한 경우 게임 종류

# 게임 종료시 총 입력한 횟수를 화면에 출력
'''
import random
obj = random.randint(1,100)
 
num = int(input("사용자 숫자 입력 : "))

count = 0
while True:
    if obj > num:
        print("업")
        count += 1
        num = int(input("사용자 숫자 입력 : "))
        
    if obj < num:
        print("다운")
        count += 1
        num = int(input("사용자 숫자 입력 : "))
       
    if obj == num:
        break

print("게임 종료 - 입력한 횟수 : {}".format(count))
'''

import random
com = int(random.random() *100) + 1
cnt = 0 # 횟수
while True:
    user = int(input("정수입력 : "))
    cnt +=1

    if user > com:
        print("[다운]")
    elif user <com:
        print("[업]")
    else:
        print("[정답]")
        print("총 입력 횟수 : {} 회".format(cnt))
        break

    































