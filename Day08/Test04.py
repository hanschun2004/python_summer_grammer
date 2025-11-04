# 문제1) 1~10 까지 반복해 5~9 출력

i = 1
while True:
    if i>=5 and i<=9:
        print(i)
    if i == 10:
        break
    i+=1

i=1
while i<=10:
    if 9>=i>=5:
        print(i)
    i+=1

# 문제2) 10~1까지 반복해 6~3 거꾸로 출력
i = 10
while True:
    if i>=3 and i<=6:
        print(i)
    if i==1:
        break
    i -= 1

i = 10 
while i>1:
    if 6>=i>=3:
        print(i)
    i -= 1



# 문제3) 1~10 까지 반복해 짝수만 출력
i = 1
while True:
    if i % 2 ==0:
        print(i)
    if i == 10:
        break
    i += 1

i = 1 
while i<=10:
    if i%2==0:
        print(i)
    i+=1

# 문제4) 1~5 까지의 합 출력
i = 1
tot = 0 
while True:
    tot += i
    if i==5:
        break
    i+=1
print(tot)

i =1
tot=0
while i<=6:
    tot = tot + i
    if i==5:
        print(tot)
    i+=1
































