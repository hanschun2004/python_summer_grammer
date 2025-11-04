# 1부터 100까지의 정수 출력
for i in range(1,101):
    print(i)
    
# 53 부터 25까지의 정수
for i in range(53,24,-1):
    print(i)

# 30 부터 60가지의 홀수
for i in range(31,60,2):
    print(i)
for i in range(30,61):
    if i % 2 ==0:
        print(i)

# 100부터 0까지의 홀수
for i in range(101,0,-2):
    print(i)

# 100부터 0가지의 5의 배수
for i in range(100,0,-5):
    print(i)
for i in range(100,-1,-1):
    if i % 5 == 0:
        print(i)
    
# A ~ Z 까지의 알파벳
for i in range(65,91):
    print(chr(i))
for i in range(ord("A"),ord("Z")+1):
    print(chr(i))

# 숫자 1개를 입력 받아 1부터 해당 수 까지 출력
a = int(input("수 입력 : "))
for i in range(1,a+1):
    print(i)
    
su = int(input("정수 입력 : "))
for i in range(1, su+1):
    print(i)


# 숫자 1개를 입력 받아 1 부터 해당 수까지 홀수 출력
a = int(input("수 입력 : "))
for i in range(1,a+1,2):
    print(i)

su = int(input("정수 입력 : "))
for i in range(1, su+1):
    if i % 2 == 0:
        print(i)


'''
a = int(input("수 입력 : "))
for i in range(1,a+1):
    print(pow(2,i))



'''












