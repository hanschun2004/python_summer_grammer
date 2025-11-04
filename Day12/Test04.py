# 1~ 45 까지 임의의 값을 중복 없이 6개 생성하여 출력하는 코드를 작성하세요
'''
import random
ls = []

cnt = 0
while cnt > 6:
    value = random.randint(1,45)
    for i in range(0,len(ls)):
        if value == ls[i]:
            cnt += 0
            print("노카운트")
        else:
            ls.append(value)
            cnt += 1
            print("카운트")
print(ls)
'''

import random
ls = []

cnt = 0
while True:
    rand = random.randint(1,45)
    if ls.count(rand) == 0:
        ls.append(rand)
    if len(ls) == 6:
        break

ls.sort()
print(ls)



























