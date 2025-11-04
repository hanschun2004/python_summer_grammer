# [아이템 강화 시뮬레이션]
# 1. 아이템은 1번 강화하는 데 현금 1000원이 필요하다.
# 2. 아이템 처음에 레벨이 0이다
# 3. 강화가 성공할 확률은 35% 이고 성공하면 레벨이 1증가
# 4. 강화가 실패할 확률은 30% 이고 성공하면 레벨이 1감소
# 5. 그 외 경우에는 아무런 변화가 없다.

# 0 레벨의 아이템을 10 레벨로 만들기 위해 내가 쏟아 부어야 되는 현금을 계산하세요

# 단, 0레벨일땐 레벨이 -1 레벨이 될 수 없다.
'''
import random

level= 0
cnt = 0
while True:
    up = input("강화 하시겠습니까? : ")
    success = random.randrange(1,100)
    if up == "o":
        cnt += 1
        print("강화 진행중")
        if success <= 50 and success >=1:
            level += 1
            print("강화 성공 , 현재 레벨 : {}".format(level))
            if level == 10:
                money = cnt *1000
                print("레벨 10 달성 , 쏟아부은 현금 : {}".format(money))
                break
                
        elif success < 65 and success > 50:
            if level == 0:
                print("강화 실패 , 현재 레벨 : {}".format(level))       
            else:
                level -= 1
                print("강화 실패 , 현재 레벨 : {}".format(level))
        else:
            print("아무런 변화 없음")
'''

# 1. 무한 반복을 돌린다.
# 2. 랜덤 확률을 뽑는다. (0 ~ 99 , 1~100 , 실수)
# 3. money에 1000원 누적
# 4. 0~ 34까지는 성공확률
# 4-1. 레벨 1 증가
# 4-2. 레벨이 10레벨이면 현금 출력 후 반복문 종료
# 5. 70 ~ 99 까지는 실패확률
# 5-1. 0레벨이 아닐 시 레벨 1 감소
# 5-2. 0레벨일 시 0레벨 이므로 더이상 감소할 수 없습니다. 출력
# 6. 35 ~ 69 까지는 아무런 변화가 없다. (else)
# 6-1. 아무런 변화 없다. 출력
'''
import random
lev = 0
money = 0
price = 1000
while True:
    rate = int(random.random()*100) # 0 ~99
    money += price

    if rate < 35:
        lev += 1
        print("강화 성공 ! + {}".format(lev))
        if lev ==10:
            print("총 금액 : {}원".format(money))
            break
    elif rate>=70:
        if lev == 0:
            print("0레벨이므로 더이상 감소할 수없습니다")
            continue # 반복문은 맨 처음으로 돌아가는데 아래 있는 모든 코드들은
        lev -= 1
        print("강화 실패 ! + {}".format(lev))
    else:
        print("아무런 변화가 없다! + {}".format(lev))
'''

import random
lev = 0
money = 0
price = 1000
while True:
    rate = random.random() # 0 ~1
    money += price

    if rate < 0.35:
        lev += 1
        print("강화 성공 ! + {}".format(lev))
        if lev ==10:
            print("총 금액 : {}원".format(money))
            break
    elif rate>=0.70:
        if lev == 0:
            print("0레벨이므로 더이상 감소할 수없습니다")
            continue # 반복문은 맨 처음으로 돌아간다.
        lev -= 1
        print("강화 실패 ! + {}".format(lev))
    else:
        print("아무런 변화가 없다! + {}".format(lev))
        




















































