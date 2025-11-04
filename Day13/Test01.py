# 빙고판 채우기
# 1부터 25까지 중복없이 5*5가 채워져야 한다.
import random

ls = [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]
'''
num = 1 

while True:
    a = random.randint(0,4)
    b = random.randint(0,4)
    if ls[a][b] == 0:
        ls[a][b] = num
        num += 1
    if num == 25:
        break

for i in range(len(ls)): # 세로 크기
    print("[",end='')
    for j in range(len(ls[i])):     # 가로 크기
        print("{},".format(ls[i][j]), end='')
    print("]")
'''
'''
i = 1
while i<= 25:
    a = int(random.random()*5)
    b = int(random.random()*5) # 0~4

    if ls[a][b] ==0:
        ls[a][b] = i
    else:
        continue # continue를 만나면 반복문의 증감식이 실행되지 않고
                # 반복문 맨 처음으로 돌아가서
                # 랜덤 인덱스를 다시 뽑는다. 
    i += 1

for i in range(0,5):
    for j in range(0,5):
        print(ls[i][j], end ="\t")
    print()
'''

'''
i = 1
while i<= 25:
    a = int(random.random()*5)
    b = int(random.random()*5) # 0~4

    if ls[a][b] ==0:
        ls[a][b] = i
    else:
        i -= 1 # i의 값을 감소시킨 다음에
                # 아래 증감식을 만나 같은 값으로 반복이 한번 더 돌게 해준다.
    i+=1

for i in range(0,5):
    for j in range(0,5):
        print(ls[i][j], end ="\t")
    print()
'''

'''
i = 1
while i<= 25:
    a = int(random.random()*5)
    b = int(random.random()*5) # 0~4

    if ls[a][b] ==0:
        ls[a][b] = i
        i+=1 #증감식을 만나지 못하면 같은값으로 반복이 한번 더돈다. 

for i in range(0,5):
    for j in range(0,5):
        print(ls[i][j], end ="\t")
    print()
'''

i = 1
while i<= 25:
    a = int(random.random()*5)
    b = int(random.random()*5) # 0~4

    if ls[a][b] ==0:
        ls[a][b] = i
        i+=1 # 증감식을 만나지 못하면 같은값으로 반복이 한번 더돈다. 

for i in range(0,5):
    for j in range(0,5):
        print(ls[i][j], end ="\t")
    print()





























       
    






















